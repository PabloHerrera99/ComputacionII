import os
import argparse
from datetime import datetime
from subprocess import Popen

def main():
    parser = argparse.ArgumentParser(description='copia')
    parser.add_argument("-c", "--command", type = str, required=True, help = "command")
    parser.add_argument("-f", "--output", type = str, required=True, help = "destination file")
    parser.add_argument("-l", "--log", type = str, required=True, help = "log file")
    args = parser.parse_args()
    
    com = os.popen(args.command)
    
    op = open(args.output, "w")
    op.write(com.read())
    op.close

    lf = open(args.log, "w")
    lf.write(str(datetime.now()) + ": Ejecutado Correctamente")
    lf.close 

if __name__ == '__main__':
    main()
