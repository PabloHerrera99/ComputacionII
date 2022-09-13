import socketserver
import multiprocessing
import signal, os
import argparse
import subprocess
import pickle
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.com = self.request.recv(1024).strip()
        self.com = pickle.loads(self.com)
        self.pr = subprocess.Popen(self.com, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.out, self.err = self.pr.communicate()
        print(self.com)
        if self.pr.returncode != 0:
            self.ans = "ERROR" + self.err
            self.request.send(self.ans)
        else:
            self.ans = "OK" + self.out
            self.request.send(self.ans)
            
class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
       

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="asd")
    parser.add_argument("-p", "--port", type=int, required=True, help="port")
    parser.add_argument("-c", "--concurrencia", type=str, required=True, help="p fork o t thread")
    arg = parser.parse_args()
    PORT = arg.port
    host = ""
    socketserver.TCPServer.allow_reuse_address = True
  
    if arg.concurrencia == "p":
        with ForkedTCPServer((host, PORT), MyTCPHandler) as server:
            server.serve_forever()
            server.shutdown()
    
    if arg.concurrencia == "t":
        with ThreadedTCPServer((host, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()

