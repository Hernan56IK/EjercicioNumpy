import multiprocessing as mp
import numpy as np
import time

N = 100_000_000

def suma_parcial(datos):
    return np.sum(datos)

def ejecutar(num_procesos):

    arr = np.arange(N)

    trozos = np.array_split(arr, num_procesos)

    inicio = time.time()

    with mp.Pool(num_procesos) as pool:
        resultados = pool.map(suma_parcial, trozos)

    total = sum(resultados)

    fin = time.time()

    return fin - inicio


if __name__ == "__main__":

    procesos = [1,2,4,8]

    for p in procesos:

        tiempos = []

        for i in range(5):

            tiempo = ejecutar(p)

            print("Procesos:",p,"Ejecucion:",i+1,"Tiempo:",tiempo)

            tiempos.append(tiempo)

        tiempos.sort()

        tiempos_validos = tiempos[1:4]

        promedio = sum(tiempos_validos)/3

        print("Promedio con",p,"procesos =",promedio)
        print()
