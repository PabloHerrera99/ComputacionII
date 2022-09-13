import re
import socket
import argparse
import sys
import pickle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="fhgf")
    parser.add_argument("-j", "--host", type=str, required=True, help="host")
    parser.add_argument("-p", "--port", type=int, required=True, help="puerto del host")
    arg = parser.parse_args()
    HOST, PORT = arg.host, arg.port
    
    while True:
        command = input("> ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            command = pickle.dumps(command.encode())
            s.send(bytes(command))

            msg = s.recv(1024)
            r = pickle.load(msg).decode()
        print(r)

