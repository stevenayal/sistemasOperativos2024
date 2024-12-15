# fifo.py
import csv
from collections import deque


def leer_secuencia_csv(nombre_archivo):
    """Lee una secuencia de páginas desde un archivo CSV."""
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            return list(map(int, fila))


# fifo.py
def fifo(secuencia, marcos):
    """Implementa el algoritmo FIFO para reemplazo de páginas."""
    memoria = deque()
    fallos = 0

    for pagina in secuencia:
        if pagina not in memoria:
            fallos += 1
            if len(memoria) >= marcos:
                memoria.popleft()  # Elimina la página más antigua
            memoria.append(pagina)
        print(f"Memoria: {list(memoria)}")  # Imprime el estado de la memoria
    return fallos



if __name__ == "__main__":
    # Nombre del archivo CSV con la secuencia de páginas
    nombre_archivo = "../CSV/secuencia_paginas.CSV"

    # Leer la secuencia de páginas
    secuencia_paginas = leer_secuencia_csv(nombre_archivo)

    # Configurar el número de marcos de memoria
    marcos = 3

    # Ejecutar el algoritmo FIFO
    fallos_fifo = fifo(secuencia_paginas, marcos)

    # Mostrar resultados
    print(f"FIFO: {fallos_fifo} fallos de página")
