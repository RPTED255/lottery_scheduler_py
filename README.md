### ¿Cómo correr el código?

Para ejecutar el código en Windows.
1. Instala Python.
2. En PowerShell ejecuta el siguiente comando:

```
Get-Command python | Select-Object -ExpandProperty Definition
```
&emsp;&ensp; Si aparece la ruta
```
%AppData%\Local\Microsoft\WindowsApps
```
&emsp;&ensp; es recomendable eliminar los archivos python.exe de la carpeta WindowsApps, pues tienen peso de 0 bytes y pueden ser una versión obsoleta del comando. Si aparece el error 0x80070780, elimine la carpeta completa.

3. Pulse la tecla Windows y busque variables de entorno, entre en Editar Variables del Sistema -> Variables de entorno -> Variables de usuario para [Usuario] -> Seleccione Path -> Editar -> Nuevo. En el campo de la nueva variable, escriba:
```
C:\Users\[Usuario]\AppData\Local\Programs\Python\PythonVXX
```
&emsp;&ensp; donde VXX es la versión que tiene, para nuestro caso fue Python311. Añada la nueva variable. Y [Usuario] el usuario del sistema.

4. Reinicie la computadora.
5. Vaya a PowerShell de nuevo y con cd cambie a la carpeta donde tiene los contenidos clonados de este repositorio.
6. Ejecute el siguiente comando:
```
Get-Content Procesos.txt | python lotery_no_preemptive.py
```
&emsp;&ensp; y espere unos segundos, deberá aparecer un mensaje diciendo **Matplotlib is building the font cache; this may take a moment.**

7. Si no tiene matplotlib aparecerá un error, deberá descargarlo mediante pip para evitar el error de módulo no encontrado con el siguiente comando:
```
python -m pip install -U pip; python -m pip install -U matplotlib
```
&emsp;&ensp; esto para prevenir también el no tener pip instalado. Al finalizar la instalación deberá aparecer un mensaje:
```
Successfully installed ... matplotlib-3.10.8 ... 
```
&emsp;&ensp; y ejecute de nuevo el comando del paso 6.

### Detalles

El algoritmo de planificación "Lottery Scheduler" se basa en crear boletos y dárselos a cada proceso. Esta asignación de boletos
tiene como objetivo que el Dispatcher seleccione el proceso de la Ready Queue de forma aleatoria (en lo posible) para cederle la CPU y de esta forma todos los procesos tengan oportunidad (incluso siendo mínima) de ser ejecutados. Puede tener variaciones de funcionamiento como el que los procesos con mayor o menor prioridad tengan una mayor cantidad de boletos asignados, dependiendo el enfoque del diseñador y el sistema donde se implementará.

El algoritmo puede ser tanto preemptivo como no preemptivo. En esta implementación se escogió el enfoque no preemptivo.

### Casos de prueba

Los casos de prueba utilizados se encuentran en el archivo Procesos.txt. Además, para estos casos se realizó una gráfica de la frecuencia de
procesos en un determinado tiempo.

### Tiempos

1. Llegada (Arrival): El momento cuando un proceso entra a la Ready Queue.
2. Inicio (Start): El momento en que el proceso pasa de estado Ready a Running.
3. Fin (Finish): El momento en que el proceso pasa de estado Running a Exit. Se considera el total de llegada, espera y ráfaga.
4. Ráfaga (Burst): Cuánto tiempo ha permanecido el proceso en el estado Running. 
5. Espera (Wait): Cuánto tiempo ha esperado el proceso en la Ready Queue para ser realizado por la CPU.
6. Retorno (Turnaround): La diferencia entre el tiempo de fin y llegada.
7. Respuesta (Response): La diferencia de tiempo entre el primer tiempo de inicio y llegada.

### Salidas

1. **Orden de ejecución**: Después del mensaje en PowerShell de Matplotlib generando la gráfica, debe aparecer una tabla escrita en carácteres titulada
"Orden de ejecución". Está generada con los procesos en orden de ejecución y sus intervalos [X-Y] con ***X*** el tiempo de inicio y ***Y*** el tiempo de fin.

2. **Resultados individuales**: Para saber el rendimiento del simulador, imprimimos los tiempos de espera, retorno y respuesta de cada proceso para
observar qué se podría mejorar.

3. **Promedio**: Para cada métrica de tiempo mencionada en el punto anterior, se tiene impreso el promedio de cada una en la consola de PowerShell al final de los resultados individuales. 

### Comparación

Debido a que solo se hizo un algoritmo, no se va a comparar con otro.
