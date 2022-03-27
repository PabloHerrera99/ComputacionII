#!/user/bin/python3
import getopt
import sys

def main():
    o = ''
    n = ''
    m = ''
    (opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')
    for (op, ar) in opt:
        if op in ['-o', '-n', '-m']:
            if op == '-o':
                o = ar
            if op == '-n':
                n = ar
            if op == '-m':
                m = ar
    print ('La operacion es: ', n,o,m) 
    oper= (n + ' ' + o + ' ' + m)
    print(str(eval(oper)))
if __name__ == '__main__':
    main()