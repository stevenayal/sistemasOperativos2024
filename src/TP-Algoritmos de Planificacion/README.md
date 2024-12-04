# Proyecto de Algoritmos de Planificación de Procesos

Este proyecto implementa dos algoritmos de planificación de procesos en Python:

1. **Shortest Job First (SJF)**: Algoritmo de planificación que ejecuta los procesos con el menor tiempo de ráfaga primero.
2. **Round Robin (RR)**: Algoritmo de planificación que asigna un tiempo fijo de ejecución (quantum) a cada proceso de manera cíclica.

## Requisitos

- **Sistema operativo**: Windows 10
- **Python**: 3.12.7

## Dependencias

Este proyecto requiere la librería `csv` de Python, que viene preinstalada con Python, por lo que no es necesario instalar dependencias adicionales.

## Instrucciones de Ejecución

### 1. Preparación del archivo CSV

Asegúrate de tener un archivo CSV en el siguiente formato para que el código pueda leerlo correctamente. El archivo debe contener tres columnas:

- **Nombre del proceso**
- **Tiempo de llegada** (opcional en el caso de los algoritmos dados)
- **Tiempo de ráfaga** (este es el tiempo que se tarda en ejecutar el proceso)

Ejemplo de archivo `algoritmos_planificacion.CSV`:

```csv
Proceso,Tiempo Llegada,Tiempo Ráfaga
P1,0,5
P2,1,3
P3,2,8
P4,3,6
```
### 2. Ejecucion de los Algoritmos
#### Algoritmo SJF (Shortest Job First)
Este algoritmo ejecuta los procesos según el tiempo de ráfaga, priorizando aquellos con menor tiempo.
- **Asegúrate de que el archivo CSV esté correctamente formateado.**
- **El código lee los procesos y tiempos de ráfaga desde el archivo CSV y luego calcula la secuencia de ejecución.**

Para ejecutar el algoritmo SJF, simplemente corre el archivo Python que contiene la función procesoMasCorto.

#### Algoritmo Round Robin
Este algoritmo asigna a cada proceso un tiempo fijo de ejecución (quantum) y los ejecuta en turnos cíclicos.

- **Al ejecutar el código, se pedirá que ingreses el valor del quantum (tiempo asignado por turno).**

#### Ejemplo de ejecucion:
Ingrese el valor del quantum: 4

### 3. Ejecución del Código
Para ejecutar cualquiera de los algoritmos, sigue estos pasos:
1. Abre la terminal en Windows (cmd o PowerShell).
2. Navega a la carpeta donde se encuentra el archivo Python.
3. Ejecuta el script Python con el siguiente comando:
 
python round_robin.py
python procesoMasCorto.py

#### Asegúrate de tener Python 3.12.7 instalado en tu sistema.

### 4. Salida esperada
- **El programa mostrará la secuencia de ejecución de los procesos según el algoritmo aplicado.**

Ejemplo de salida para el algoritmo Round Robin:

Ingrese el valor del quantum: 4
Secuencia de ejecución:
P1, P2, P3, P4, P1, P2, P3, P1

### 5. Consideraciones
- **Asegúrate de que el archivo CSV esté correctamente formateado antes de ejecutar el código.**
- **Si el archivo CSV no se encuentra o está mal formateado, el código mostrará un error indicándolo.**

### Contribuciones
Si deseas mejorar este proyecto, no dudes en realizar un fork y enviar un pull request. Acepto sugerencias y mejoras de cualquier tipo.

### Licencia
Este proyecto es de uso libre. Puedes utilizar, modificar y distribuir este código bajo los términos de la Licencia MIT.