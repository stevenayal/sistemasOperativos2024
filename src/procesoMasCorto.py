import csv


def procesoMasCorto(processes, burst_times):
    """
    Implementa el algoritmo de El Proceso Más Corto Primero (SJF).

    :param processes: Lista de nombres de procesos.
    :param burst_times: Lista de tiempos de ráfaga de cada proceso.
    """
    # Emparejar los procesos con sus tiempos de ráfaga
    process_data = list(zip(processes, burst_times))

    # Ordenar los procesos por tiempo de ráfaga (en orden ascendente)
    process_data.sort(key=lambda x: x[1])

    sequence = []  # Lista para almacenar la secuencia de ejecución

    # Ejecutar los procesos según el orden de su ráfaga
    for process, burst in process_data:
        sequence.extend([process] * burst)  # Agregar el proceso a la secuencia por su tiempo de ráfaga

    # Imprimir la secuencia de ejecución
    print("Secuencia de ejecución:")
    print(", ".join(sequence))


def read_csv(filename):
    processes = []
    burst_times = []

    # Leer el archivo CSV
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            processes.append(row[0])
            burst_times.append(int(row[2]))  # Solo el tiempo de ráfaga

    return processes, burst_times


# Ejemplo de uso
filename = 'CSV/algoritmos_planificacion.csv'  # Ruta del archivo CSV

# Leer el CSV y ejecutar SJF
processes, burst_times = read_csv(filename)
procesoMasCorto(processes, burst_times)
