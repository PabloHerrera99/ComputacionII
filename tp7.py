import multiprocessing as mp
import time, os, sys

def rot13_func(mensaje):
    print("El mensaje recibido en la funcion de encriptar es: %s" % str(mensaje))
    mensaje_encriptado = []
    for letra in mensaje[:-1]:
        desp = ord(letra) + 13
        if ord(letra) >= 97 and ord(letra) <= 122:
            if desp > 122:
                desp = desp - 122 + 97 - 1
        else:
            if desp > 90:
                desp = desp - 90 + 65 - 1
        letra_encriptada = chr(desp)
        mensaje_encriptado.append(letra_encriptada)
    return "".join(mensaje_encriptado)

def h1_lector(w,q):
    print('h1 lee')
    sys.stdin = open(0)
    txt = sys.stdin.readline()
    w.send(txt)
    w.close()
    print("h1 encriptado: %s" % q.get())

def h2_lector(r,q):
    txt = r.recv()
    r.close
    encriptado = rot13_func(str(txt))
    q.put(encriptado)


if __name__ == '__main__':
    r, w = mp.Pipe()
    q = mp.Queue()
    h1 = mp.Process(target=h1_lector, args = (w, q))
    h2 = mp.Process(target=h2_lector, args = (r, q))
    h1.start()
    h2.start()
    h1.join()
    h2.join()