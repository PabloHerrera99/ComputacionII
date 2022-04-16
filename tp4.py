#Escribir un programa en Python que reciba los siguientes argumentos por línea de comandos:
#
#-n <N>
#-r <R>
#-h
#-f <ruta_archivo>
#-v
#El programa deberá abrir (crear si no existe) un archivo de texto cuyo path ha sido pasado por argumento con -f.
#
#El programa debe generar <N> procesos hijos. Cada proceso estará asociado a una letra del alfabeto (el primer proceso con la "A", el segundo con la "B", etc). Cada proceso almacenará en el archivo su letra <R> veces con un delay de un segundo entre escritura y escritura (realizar flush() luego de cada escritura).
#
#El proceso padre debe esperar a que los hijos terminen, luego de lo cual deberá leer el contenido del archivo y mostrarlo por pantalla.
#
#La opción -h mostrará ayuda. La opción -v activará el modo verboso, en el que se mostrará antes de escribir cada letra en el archivo: Proceso <PID> escribiendo letra 'X'.

import argparse
import subprocess as sp
import subprocess
from subprocess import Popen
import os
from os import fork
import time

def create_and_calculate(number, letter, abc, len_abc, file_name, verbose):
    file = open(file_name, "w+")
    for i in range(number):
        pos = i % len_abc
        letra = abc[pos]
        fpid = fork()
        if fpid == 0:
            pid = os.getpid()
            for k in range(letter):
                if verbose:
                    print("Proceso %d escribiendo letra '%s'" % (pid, letra))
                file.write(letra)
                file.flush()
                time.sleep(1)
            os._exit(0)


  

def main():
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len_abc = len(abc)

    parser = argparse.ArgumentParser(description='assdsada')
    parser.add_argument("-f", "--output", type = str, required=True, help = "destination file")
    parser.add_argument("-n", "--number", type=int, required=True, help="numero de procesos")
    parser.add_argument("-r", "--letters", type=int, required=True, help="numero letras a escribir por proceso")
    parser.add_argument("-v", "--verbose", action='store_true', help="ejecutar programa en modo verboso")
    args = parser.parse_args()

    create_and_calculate(args.number, args.letters, abc, len_abc, args.output, args.verbose)


if __name__ == '__main__':
    main()