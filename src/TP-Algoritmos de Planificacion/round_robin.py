import csv
from collections import deque

def round_robin(processes, burst_times, quantum):
    """
    Implementa el algoritmo de Round Robin y genera la secuencia de ejecucion.

    :param processes: Lista de nombres de procesos.
    :param burst_times: Lista de tiempos de rafaga de cada proceso.
    :param quantum: Unidad de tiempo asignada a cada proceso por turno.
    """
    n = len(processes)
    remaining_burst = burst_times[:]
    sequence = []  # Lista para almacenar la secuencia de ejecucion

    # Cola de procesos
    queue = deque([(processes[i], remaining_burst[i]) for i in range(n)])

    # Mientras haya procesos pendientes de ejecutar
    while queue:
        process, burst = queue.popleft()
        execute_time = min(quantum, burst)  # Determinar el tiempo de ejecución del proceso

        # Añadir el proceso a la secuencia de ejecucion
        sequence.extend([process] * execute_time)

        # Actualizar la rafaga restante
        remaining_burst[processes.index(process)] -= execute_time

        # Si el proceso tiene rafaga restante, volver a insertarlo en la cola
        if remaining_burst[processes.index(process)] > 0:
            queue.append((process, remaining_burst[processes.index(process)]))

    # Imprimir la secuencia de ejecucion
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
            burst_times.append(int(row[2]))  # Solo el tiempo de rafaga

    return processes, burst_times


# Ejemplo de uso
filename = '../CSV/algoritmos_planificacion.CSV'  # Ruta del archivo CSV

# Solicitar al usuario que ingrese el quantum
quantum = int(input("Ingrese el valor del quantum: "))

# Leer el CSV y ejecutar Round Robin
processes, burst_times = read_csv(filename)
round_robin(processes, burst_times, quantum)
