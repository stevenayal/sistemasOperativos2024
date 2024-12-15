import csv

def leer_secuencia_csv(nombre_archivo):
    """Lee una secuencia de páginas desde un archivo CSV."""
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            return list(map(int, fila))


def lru(secuencia, marcos):
    """Implementa el algoritmo LRU para reemplazo de páginas."""
    memoria = []
    ultimos_usos = {}
    fallos = 0

    for i, pagina in enumerate(secuencia):
        if pagina not in memoria:
            fallos += 1
            if len(memoria) >= marcos:
                # Encuentro la página menos recientemente usada
                menos_usada = min(memoria, key=lambda p: ultimos_usos[p])
                memoria.remove(menos_usada)
            memoria.append(pagina)
        # Actualizo el último uso de la página
        ultimos_usos[pagina] = i
        print(f"Memoria: {memoria}")

    return fallos


if __name__ == "__main__":
    # Nombre del archivo CSV con la secuencia de páginas
    nombre_archivo = "../CSV/secuencia_paginas.CSV"

    # Leer la secuencia de páginas
    secuencia_paginas = leer_secuencia_csv(nombre_archivo)

    # Configurar el número de marcos de memoria
    marcos = 3

    # Ejecutar el algoritmo LRU
    fallos_lru = lru(secuencia_paginas, marcos)

    # Mostrar resultados
    print(f"LRU: {fallos_lru} fallos de página")
