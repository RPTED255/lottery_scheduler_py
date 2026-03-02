import sys
import random
import matplotlib.pyplot as plt

class Proceso:
    def __init__(self, pid, llegada, rafaga, prioridad):
        self.pid = pid
        self.llegada = llegada
        self.rafaga = rafaga
        self.prioridad = prioridad  # tickets
        self.inicio = None
        self.fin = None
        self.respuesta = None
        self.retorno = None
        self.espera = None


def leer_procesos():
    procesos = []
    for linea in sys.stdin:
        if linea.strip():
            datos = list(map(int, linea.split()))
            procesos.append(Proceso(*datos))
    return procesos


def lottery_no_preemptive(procesos):
    tiempo = 0
    completados = 0
    n = len(procesos)
    linea_tiempo = []

    procesos.sort(key=lambda p: p.llegada)

    while completados < n:

        disponibles = [p for p in procesos if p.llegada <= tiempo and p.fin is None]

        if not disponibles:
            tiempo += 1
            continue

        total_tickets = sum(p.prioridad for p in disponibles)
        ganador = random.randint(1, total_tickets)

        acumulado = 0
        for p in disponibles:
            acumulado += p.prioridad
            if acumulado >= ganador:
                seleccionado = p
                break

        seleccionado.inicio = tiempo
        seleccionado.fin = tiempo + seleccionado.rafaga

        seleccionado.respuesta = seleccionado.inicio - seleccionado.llegada
        seleccionado.retorno = seleccionado.fin - seleccionado.llegada
        seleccionado.espera = seleccionado.retorno - seleccionado.rafaga

        tiempo += seleccionado.rafaga
        completados += 1
        linea_tiempo.append((seleccionado.pid, seleccionado.inicio, seleccionado.fin))

    return linea_tiempo


def imprimir_resultados(procesos, linea_tiempo):
    print("\nOrden de ejecución:")
    for pid, inicio, fin in linea_tiempo:
        print(f"P{pid}: [{inicio} - {fin}]")

    print("\nResultados individuales:")
    print("PID\tEspera\tRetorno\tRespuesta")
    for p in procesos:
        print(f"{p.pid}\t{p.espera}\t{p.retorno}\t{p.respuesta}")


def graficar(procesos):

    espera = [p.espera for p in procesos]
    retorno = [p.retorno for p in procesos]
    respuesta = [p.respuesta for p in procesos]

    plt.figure()
    plt.hist(espera, bins=10)
    plt.title("Distribución Tiempo de Espera")
    plt.xlabel("Tiempo")
    plt.ylabel("Frecuencia")
    plt.show()

    plt.figure()
    plt.hist(retorno, bins=10)
    plt.title("Distribución Tiempo de Retorno")
    plt.xlabel("Tiempo")
    plt.ylabel("Frecuencia")
    plt.show()

    plt.figure()
    plt.hist(respuesta, bins=10)
    plt.title("Distribución Tiempo de Respuesta")
    plt.xlabel("Tiempo")
    plt.ylabel("Frecuencia")
    plt.show()


if __name__ == "__main__":
    procesos = leer_procesos()
    linea_tiempo = lottery_no_preemptive(procesos)
    imprimir_resultados(procesos, linea_tiempo)
    graficar(procesos)