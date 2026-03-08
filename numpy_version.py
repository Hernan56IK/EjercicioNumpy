import os
import numpy as np
import time

N = 100_000_000

def ejecutar(hilos):

    os.environ["OMP_NUM_THREADS"] = str(hilos)
    os.environ["MKL_NUM_THREADS"] = str(hilos)
    os.environ["OPENBLAS_NUM_THREADS"] = str(hilos)

    arr = np.arange(N)

    inicio = time.time()

    total = np.sum(arr)

    fin = time.time()

    return fin - inicio


if __name__ == "__main__":

    hilos = [1,2,4,8]

    for h in hilos:

        tiempos = []

        for i in range(5):

            tiempo = ejecutar(h)

            print("Hilos:",h,"Ejecucion:",i+1,"Tiempo:",tiempo)

            tiempos.append(tiempo)

        tiempos.sort()

        tiempos_validos = tiempos[1:4]

        promedio = sum(tiempos_validos)/3

        print("Promedio con",h,"hilos =",promedio)
        print()
