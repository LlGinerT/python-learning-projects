import time
import threading
import multiprocessing

from procesadorDatos import ProcesadorDatos


LOTES = 5
DURACION_IO = 2
CARGA_CPU = 20_000_000


# =========================
# MONOHILO
# =========================
def ejecutar_monohilo(funcion, parametro):
    inicio = time.time()

    for i in range(LOTES):
        funcion(i + 1, parametro)

    fin = time.time()
    return fin - inicio


# =========================
# MULTIHILO
# =========================
def ejecutar_multihilo(funcion, parametro):
    inicio = time.time()
    hilos = []

    for i in range(LOTES):
        hilo = threading.Thread(target=funcion, args=(i + 1, parametro))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    fin = time.time()
    return fin - inicio


# =========================
# MULTIPROCESO
# =========================
def ejecutar_multiproceso(funcion, parametro):
    inicio = time.time()
    procesos = []

    for i in range(LOTES):
        proceso = multiprocessing.Process(target=funcion, args=(i + 1, parametro))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    fin = time.time()
    return fin - inicio


def tabla_resultados(resultados):
    """
    Muestra una tabla resumen con los tiempos obtenidos
    en cada tipo de ejecución.
    """
    print("\n" + "=" * 86)
    print("TABLA COMPARATIVA FINAL")
    print("=" * 86)
    print(
        f"{'Versión':<18}{'Tipo de tarea':<18}{'Tiempo (s)':<15}{'Interpretación':<35}"
    )
    print("-" * 86)

    for resultado in resultados:
        print(
            f"{resultado['version']:<18}"
            f"{resultado['tipo']:<18}"
            f"{resultado['tiempo']:<15.2f}"
            f"{resultado['interpretacion']:<35}"
        )

    print("=" * 86)


if __name__ == "__main__":

    print("\n==============================")
    print("VERSIÓN 1: I/O-bound (sleep)")
    print("==============================\n")

    print("\n==============================")
    print("MONOHILO")
    print("==============================")
    t1 = ejecutar_monohilo(ProcesadorDatos.procesar_datos_io, DURACION_IO)
    print(f"Monohilo IO: {t1:.2f} s\n")

    print("\n==============================")
    print("MULTIHILO")
    print("==============================\n")
    t2 = ejecutar_multihilo(ProcesadorDatos.procesar_datos_io, DURACION_IO)
    print(f"Multihilo IO: {t2:.2f} s\n")

    print("\n==============================")
    print("MULTIPROCESO")
    print("==============================\n")
    t3 = ejecutar_multiproceso(ProcesadorDatos.procesar_datos_io, DURACION_IO)
    print(f"Multiproceso IO: {t3:.2f} s\n")

    print("\n==============================")
    print("VERSIÓN 2: CPU-bound (cálculo)")
    print("==============================\n")

    print("\n==============================")
    print("MONOHILO")
    print("==============================\n")
    t4 = ejecutar_monohilo(ProcesadorDatos.procesar_datos_cpu, CARGA_CPU)
    print(f"Monohilo CPU: {t4:.2f} s\n")

    print("\n==============================")
    print("MULTIHILO")
    print("==============================\n")
    t5 = ejecutar_multihilo(ProcesadorDatos.procesar_datos_cpu, CARGA_CPU)
    print(f"Multihilo CPU: {t5:.2f} s\n")

    print("\n==============================")
    print("MULTIPROCESO")
    print("==============================\n")
    t6 = ejecutar_multiproceso(ProcesadorDatos.procesar_datos_cpu, CARGA_CPU)
    print(f"Multiproceso CPU: {t6:.2f} s\n")

    resultados = [
        {
            "version": "Monohilo IO",
            "tipo": "I/O-bound",
            "tiempo": t1,
            "interpretacion": "Secuencial, sin concurrencia",
        },
        {
            "version": "Multihilo IO",
            "tipo": "I/O-bound",
            "tiempo": t2,
            "interpretacion": "Concurrencia eficiente",
        },
        {
            "version": "Multiproceso IO",
            "tipo": "I/O-bound",
            "tiempo": t3,
            "interpretacion": "Similar a multihilo",
        },
        {
            "version": "Monohilo CPU",
            "tipo": "CPU-bound",
            "tiempo": t4,
            "interpretacion": "Secuencial, usa un núcleo",
        },
        {
            "version": "Multihilo CPU",
            "tipo": "CPU-bound",
            "tiempo": t5,
            "interpretacion": "Limitado por el GIL",
        },
        {
            "version": "Multiproceso CPU",
            "tipo": "CPU-bound",
            "tiempo": t6,
            "interpretacion": "Paralelismo real",
        },
    ]

    tabla_resultados(resultados)
