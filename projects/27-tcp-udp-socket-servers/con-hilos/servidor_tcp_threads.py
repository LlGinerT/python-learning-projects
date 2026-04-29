"""Servidor TCP concurrente que atiende cada cliente en un hilo independiente."""

import signal
import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 12355
BUFFER_SIZE = 1024
CONFIRMACION = "Mensaje Tipo A recibido correctamente por el servidor con hilos."
RETARDO_PRUEBA = 5
SOCKET_TIMEOUT = 1
# Esta bandera permite salir del bucle principal sin depender de una excepcion.
servidor_activo = True


def solicitar_cierre(signum, frame) -> None:
    """Marca la parada del servidor cuando se recibe la señal de interrupción."""
    del signum, frame
    global servidor_activo
    # Ctrl+C no interrumpe el flujo con traceback: solo marca el cierre ordenado.
    servidor_activo = False
    print("\nCerrando servidor TCP con hilos...")


def atender_cliente(conexion: socket.socket, direccion: tuple[str, int]) -> None:
    """Gestiona la comunicación completa con un cliente TCP concreto."""
    with conexion:
        try:
            # Cada hilo gestiona una conexion TCP completa de forma aislada.
            datos = conexion.recv(BUFFER_SIZE)

            if not datos:
                print(f"[{direccion[0]}:{direccion[1]}] Conexion sin contenido.")
                return

            mensaje = datos.decode("utf-8").strip()
            print(f"[{direccion[0]}:{direccion[1]}] Mensaje Tipo A: {mensaje}")
            # Este retardo ayuda a comprobar visualmente que otros clientes no quedan bloqueados.
            print(f"[{direccion[0]}:{direccion[1]}] Iniciando retardo de prueba de {RETARDO_PRUEBA} segundos.")
            time.sleep(RETARDO_PRUEBA)
            conexion.sendall(CONFIRMACION.encode("utf-8"))
            print(f"[{direccion[0]}:{direccion[1]}] Confirmacion enviada.")
        except OSError as error:
            print(f"[{direccion[0]}:{direccion[1]}] Error al atender al cliente: {error}")


def iniciar_servidor() -> None:
    """Arranca el servidor TCP y crea un hilo por cada conexión entrante."""
    # Registramos SIGINT para controlar manualmente el cierre del servidor.
    signal.signal(signal.SIGINT, solicitar_cierre)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()
        # El timeout corto evita que accept() bloquee indefinidamente al cerrar.
        servidor.settimeout(SOCKET_TIMEOUT)

        print(f"Servidor TCP con hilos escuchando en {HOST}:{PORT}")
        print("Pulsa Ctrl+C para detenerlo.")

        try:
            while servidor_activo:
                try:
                    conexion, direccion = servidor.accept()
                except socket.timeout:
                    # Volvemos al inicio para comprobar si SIGINT ha pedido detener el servidor.
                    continue
                # Se crea un hilo por cliente para que el servidor pueda seguir aceptando conexiones.
                hilo = threading.Thread(
                    target=atender_cliente,
                    args=(conexion, direccion),
                    daemon=True,
                )
                hilo.start()
                print(f"Cliente conectado desde {direccion[0]}:{direccion[1]} en el hilo {hilo.name}")
        except OSError as error:
            print(f"Error en el servidor TCP con hilos: {error}")
        finally:
            print("Servidor TCP con hilos detenido.")


if __name__ == "__main__":
    iniciar_servidor()
