import argparse
from ast import Global
from email import parser
import sys
import time
import subprocess as sp
import multiprocessing as mp
import os 
import math

matriz = []
global args
def calc(linea):
    global args
    if len(linea) > 4:
        time.sleep(3)
    line_calc = []
    if args.calc == 'pot':
        for element in linea:
            line_calc.append(math.pow(int(element), int(element)))
    elif args.calc == 'raiz':
        for element in linea:
            line_calc.append(math.sqrt(int(element), int(element)))
    elif args.calc == 'log':
        for element in linea:
            line_calc.append(math.log10(int(element), int(element)))
            

def main():
    parser = argparse.ArgumentParser(description="-p Cantidad de procesos, -f Directorio del archivo a leer, -c funcion a ingresar: raiz, pot, log")

    parser.add_argument("-p", "--process", type=int, required=True, help="string")
    parser.add_argument("-f", "--inputfile", type=str, required=True, help="string")
    parser.add_argument("-c", "--calc", type=str, required=True, help="string")
    global args
    args = parser.parse_args()

    print('PID Proceso padre: %d' % os.getpid())
    with open(args.inputfile, "r") as inputfile:
        for line in inputfile:
            matriz.append(line[:-1].split(' '))
    pool = mp.Pool(processes = int(args.process))
    results = []
    results = pool.map_async(calc, matriz).get()
    for line in results:
        print(line)
if __name__ == '__main__':
    main()