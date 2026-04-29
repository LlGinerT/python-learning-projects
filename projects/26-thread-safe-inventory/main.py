import threading
import time


STOCK_INICIAL = 1000
NUM_PEDIDOS = 100

stock_disponible = STOCK_INICIAL
lock_stock = threading.Lock()
programa_activo = True


def monitor_stock():
    """
    Hilo daemon que muestra periódicamente el stock disponible.
    Se detiene automáticamente cuando termina el programa principal.
    """
    while programa_activo:
        print(f"[MONITOR] Stock actual: {stock_disponible}")
        time.sleep(0.02)


def procesar_pedido_sin_sync(numero_pedido):
    """
    Simula el procesamiento de un pedido sin proteger el acceso
    a la variable global stock_disponible.
    """
    global stock_disponible

    try:
        print(f"[INICIO] Procesando pedido {numero_pedido}")
        time.sleep(0.01)

        # Lectura-modificación-escritura NO atómica
        stock_disponible -= 1

        print(
            f"[FIN] Pedido {numero_pedido} procesado | "
            f"Stock restante: {stock_disponible}"
        )
    except Exception as error:
        print(f"[ERROR] Pedido {numero_pedido}: {error}")


def procesar_pedido_sin_sync_condicion_carrera(numero_pedido):
    """
    Simula el procesamiento de un pedido sin proteger el acceso
    a la variable global stock_disponible y exagerando la condicion de carrera.
    """
    global stock_disponible

    try:
        print(f"[INICIO] Procesando pedido {numero_pedido}")

        # Lectura
        stock_actual = stock_disponible
        time.sleep(0.01)
        # modificacion
        stock_actual -= 1
        # escritura
        stock_disponible = stock_actual

        print(
            f"[FIN] Pedido {numero_pedido} procesado | "
            f"Stock restante: {stock_disponible}"
        )
    except Exception as error:
        print(f"[ERROR] Pedido {numero_pedido}: {error}")


def procesar_pedido_con_sync(numero_pedido):
    """
    Simula el procesamiento de un pedido protegiendo la variable global
    stock_disponible mediante exclusión mutua.
    """
    global stock_disponible

    try:
        print(f"[INICIO] Procesando pedido {numero_pedido}")
        time.sleep(0.01)

        # Sección crítica protegida con Lock
        with lock_stock:
            stock_disponible -= 1

        print(
            f"[FIN] Pedido {numero_pedido} procesado | "
            f"Stock restante: {stock_disponible}"
        )
    except Exception as error:
        print(f"[ERROR] Pedido {numero_pedido}: {error}")


def ejecutar_simulacion(funcion_pedido, titulo):
    """
    Lanza NUM_PEDIDOS hilos y espera a que terminen.
    """
    global stock_disponible

    stock_disponible = STOCK_INICIAL
    hilos = []

    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)
    print(f"Stock inicial: {stock_disponible}")
    print(f"Número de pedidos: {NUM_PEDIDOS}")
    print("-" * 60)

    inicio = time.time()

    for numero_pedido in range(1, NUM_PEDIDOS + 1):
        hilo = threading.Thread(target=funcion_pedido, args=(numero_pedido,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    fin = time.time()

    print("-" * 60)
    print(f"Stock final: {stock_disponible}")
    print(f"Tiempo total: {fin - inicio:.4f} segundos")
    print("=" * 60)


if __name__ == "__main__":

    hilo_monitor = threading.Thread(target=monitor_stock, daemon=True)
    hilo_monitor.start()

    ejecutar_simulacion(
        procesar_pedido_sin_sync, "EJECUCIÓN 1 - MULTIHILO SIN SINCRONIZACIÓN"
    )

    ejecutar_simulacion(
        procesar_pedido_sin_sync_condicion_carrera,
        "EJECUCIÓN 2 - MULTIHILO SIN SINCRONIZACIÖN Y CONDICION DE CARRERA",
    )

    ejecutar_simulacion(
        procesar_pedido_con_sync, "EJECUCIÓN 3 - MULTIHILO CON SINCRONIZACIÓN (LOCK)"
    )

    programa_activo = False

    print("\nResumen esperado:")
    print("- Sin sincronización: el stock final puede ser incorrecto.")
    print("- Con sincronización: el stock final debe ser 900.")
