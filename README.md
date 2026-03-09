Hernan Dario Garcia Mahecha 2041418
Juan Camilo Jimenez Toro 2042782



Simulación de Vectorización (SIMD) – Programación Paralela

Integrantes - Nombre 1 - Nombre 2 - Nombre 3

Descripción En este ejercicio se implementó la suma de un vector muy
grande (100,000,000 elementos) utilizando dos enfoques diferentes:

1.  Multiprocessing: paralelización usando múltiples procesos.
2.  NumPy: vectorización utilizando operaciones optimizadas que simulan
    el modelo SIMD (Single Instruction Multiple Data).

Para cada versión del programa se realizaron pruebas con: 1
proceso/hilo, 2 procesos/hilos, 4 procesos/hilos y 8 procesos/hilos.

Cada versión se ejecutó 5 veces. De los cinco tiempos obtenidos se
eliminó el mayor y el menor, y con los tres tiempos restantes se calculó
el promedio.

Ejecución del programa

Versión con procesos: python multiproceso.py

Versión con NumPy: python numpy_version.py

Resultados

Tiempos de ejecución – Multiprocessing

Procesos | Ejec1 | Ejec2 | Ejec3 | Ejec4 | Ejec5 | Promedio 1 | 2.1028 |
1.8346 | 1.8989 | 1.7705 | 1.8813 | 1.8716 2 | 1.6575 | 1.6321 | 1.6014
| 1.5817 | 1.6652 | 1.6303 4 | 1.6287 | 1.6323 | 1.5853 | 1.7267 |
1.6645 | 1.6418 8 | 2.0619 | 1.9992 | 1.9084 | 1.8386 | 1.8444 | 1.9173

Tiempos de ejecución – NumPy

Hilos | Ejec1 | Ejec2 | Ejec3 | Ejec4 | Ejec5 | Promedio 1 | 0.05696 |
0.05367 | 0.05475 | 0.05434 | 0.05452 | 0.05454 2 | 0.08212 | 0.05663 |
0.05872 | 0.05334 | 0.05504 | 0.05680 4 | 0.05883 | 0.05690 | 0.05795 |
0.05818 | 0.05803 | 0.05805 8 | 0.05495 | 0.06472 | 0.05892 | 0.06218 |
0.05556 | 0.05889

Speedup

El speedup mide cuánto mejora el rendimiento al aumentar el número de
procesos.

Fórmula: Speedup = T1 / Tp

donde: T1 = tiempo con 1 proceso Tp = tiempo con p procesos

Speedup – Multiprocessing

Procesos | Tiempo | Speedup 1 | 1.8716 | 1.00 2 | 1.6303 | 1.15 4 |
1.6418 | 1.14 8 | 1.9173 | 0.98

Speedup – NumPy

Hilos | Tiempo | Speedup 1 | 0.05454 | 1.00 2 | 0.05680 | 0.96 4 |
0.05805 | 0.94 8 | 0.05889 | 0.93

Eficiencia

Fórmula: Eficiencia = Speedup / Número de procesos

Eficiencia – Multiprocessing

Procesos | Eficiencia 1 | 100 % 2 | 57 % 4 | 28 % 8 | 12 %

Eficiencia – NumPy

Hilos | Eficiencia 1 | 100 % 2 | 48 % 4 | 23 % 8 | 12 %

Comparación entre versiones

Implementación | Tiempo Multiprocessing | 1.8716 s NumPy | 0.05454 s

Factor de mejora

Factor = Tiempo_multiprocessing / Tiempo_numpy Factor = 1.8716 / 0.05454
≈ 34.33

La versión con NumPy fue aproximadamente 34 veces más rápida.

Conclusiones

-   La implementación con NumPy presentó un rendimiento
    significativamente superior.
-   NumPy utiliza operaciones vectorizadas optimizadas en C que
    aprovechan el modelo SIMD.
-   La versión con multiprocessing introduce overhead de creación y
    comunicación de procesos.
-   Al aumentar el número de procesos la eficiencia disminuye debido a
    los costos de sincronización.
