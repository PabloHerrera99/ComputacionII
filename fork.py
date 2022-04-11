import argparse
import sys
import time
import subprocess as sp
import os
from os import fork
from click import command
from numpy import number

def create_and_calculate(number, verbose):
    for i in range(number):
        fpid = fork()
        if fpid == 0:
            suma = 0
            pid = os.getpid()
            
            if verbose:
                print("Starting process %d" % pid)
            for k in range(0, pid+1, 2):
                suma = k + suma
                
            if verbose:
                print("Ending process %d" % pid)
            ppid = os.getppid()
            print("%d - %d : %d" % (pid, ppid, suma))
            os._exit(0)

def main():

    parser = argparse.ArgumentParser(description="sdasdas")
    parser.add_argument("-n", "--number", type=int, required=True, help="Ingrese el numero de procesos a crear")
    parser.add_argument("-v", "--verbose", action='store_true', help="Ejecutar programa en modo verboso")
    args = parser.parse_args()
    create_and_calculate(args.number, args.verbose)
    for i in range(args.number):
        os.wait()

if __name__ == '__main__':
    main()