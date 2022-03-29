import argparse
from datetime import datetime
import subprocess
from subprocess import Popen

def main():
    parser = argparse.ArgumentParser(description='copia')
    parser.add_argument("-c", "--command", type = str, required=True, help = "command")
    parser.add_argument("-f", "--output", type = str, required=True, help = "destination file")
    parser.add_argument("-l", "--log", type = str, required=True, help = "log file")
    args = parser.parse_args()

    com = subprocess.Popen(args.command, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = com.communicate()

    op = open(args.output, "a")
    op.write(format(out)+ '\n')
    op.close()
    key = "key" + format(out)

    lf = open(args.log, "a")
    if key != "key":
        lf.write(str(datetime.now()) + ":     Ejecutado Correctamente" + '\n')
    else:
        lf.write(str(datetime.now()) + ":     " + format(err))
    lf.close()

if __name__ == '__main__':
    main()