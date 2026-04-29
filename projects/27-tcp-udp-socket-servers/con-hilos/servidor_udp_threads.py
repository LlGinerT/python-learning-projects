"""Servidor UDP concurrente que procesa cada datagrama en su propio hilo."""

import signal
import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 12356
BUFFER_SIZE = 1024
RETARDO_PRUEBA = 5
SOCKET_TIMEOUT = 1
# Esta bandera permite salir del bucle principal sin lanzar KeyboardInterrupt.
servidor_activo = True


def solicitar_cierre(signum, frame) -> None:
    """Solicita un cierre ordenado del servidor al recibir Ctrl+C."""
    del signum, frame
    global servidor_activo
    # El manejador de la señal solicita un cierre limpio del servidor.
    servidor_activo = False
    print("\nCerrando servidor UDP con hilos...")


def procesar_datagrama(datos: bytes, direccion: tuple[str, int]) -> None:
    """Decodifica y procesa un datagrama recibido desde un cliente."""
    try:
        mensaje = datos.decode("utf-8").strip()
        print(f"[{threading.current_thread().name}] Datagrama desde {direccion[0]}:{direccion[1]} -> {mensaje}")
        # El retardo deja ver que pueden coexistir varios datagramas en procesamiento.
        print(f"[{threading.current_thread().name}] Iniciando retardo de prueba de {RETARDO_PRUEBA} segundos.")
        time.sleep(RETARDO_PRUEBA)
        print(f"[{threading.current_thread().name}] Datagrama procesado.")
    except UnicodeDecodeError:
        print(f"[{threading.current_thread().name}] No se ha podido decodificar el datagrama de {direccion}.")


def iniciar_servidor() -> None:
    """Inicia el servidor UDP y delega cada datagrama a un hilo daemon."""
    # SIGINT se usa para convertir Ctrl+C en una peticion de parada controlada.
    signal.signal(signal.SIGINT, solicitar_cierre)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((HOST, PORT))
        # recvfrom() despierta cada segundo para revisar la bandera de cierre.
        servidor.settimeout(SOCKET_TIMEOUT)

        print(f"Servidor UDP con hilos escuchando en {HOST}:{PORT}")
        print("Pulsa Ctrl+C para detenerlo.")

        try:
            while servidor_activo:
                try:
                    datos, direccion = servidor.recvfrom(BUFFER_SIZE)
                except socket.timeout:
                    # El bucle sigue vivo, pero puede terminar si SIGINT cambia la bandera.
                    continue
                # Aunque UDP no acepta conexiones, procesamos cada datagrama en un hilo aparte.
                hilo = threading.Thread(
                    target=procesar_datagrama,
                    args=(datos, direccion),
                    daemon=True,
                )
                hilo.start()
        except OSError as error:
            print(f"Error en el servidor UDP con hilos: {error}")
        finally:
            print("Servidor UDP con hilos detenido.")


if __name__ == "__main__":
    iniciar_servidor()
