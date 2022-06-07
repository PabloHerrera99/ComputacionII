import argparse
import sys
import time
import subprocess as sp
import os
from os import fork
from click import command
from numpy import number

def main():
    parser = argparse.ArgumentParser(description="inversor")
    parser.add_argument("-f", "--path", type=str, required=True, help="Ingrese el path del archivo a leer")
    args = parser.parse_args()
    
    with open(args.path, "r") as file1:
        T_lines = sum(1 for line in file1)
    
    file1 = open(args.path, "r")
    count = 0
    r, w = os.pipe()
    r1 ,w1 = os.pipe()

    for i in range(T_lines):
        fpid = fork()
        if fpid == 0:
            os.close(w)
            os.close(r1)
            r = os.fdopen (r)
            linea = r.read()
            w1 = os.fdopen(w1, 'w')
            w1.write("%s" % linea[::-1])
            w1.flush()
            w1.close()
            os._exit(0)
    w = os.fdopen(w, 'w')

    for lines in file1:
        w.write(lines)
    w.close()
    os.close(w1)
    r1 = os.fdopen(r1)
    for i in range(T_lines):
        linea = r1.read()
        print("%s" % linea)
        os.wait()
    r1.close()
    file1.close()   

if __name__ == '__main__':
    main()
