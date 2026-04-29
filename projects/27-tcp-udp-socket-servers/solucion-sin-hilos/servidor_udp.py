"""Servidor UDP secuencial que muestra en consola cada datagrama recibido."""

import signal
import socket


HOST = "127.0.0.1"
PORT = 12346
BUFFER_SIZE = 1024
SOCKET_TIMEOUT = 1
# La bandera se consulta en cada vuelta para cerrar el servidor con limpieza.
servidor_activo = True


def solicitar_cierre(signum, frame) -> None:
    """Solicita la parada del servidor cuando se recibe una interrupción."""
    del signum, frame
    global servidor_activo
    # Ctrl+C solo cambia el estado del servidor y evita trazas innecesarias.
    servidor_activo = False
    print("\nCerrando servidor UDP...")


def iniciar_servidor() -> None:
    """Inicia el servidor UDP y procesa los datagramas de uno en uno."""
    # Con SIGINT controlamos explicitamente el cierre desde teclado.
    signal.signal(signal.SIGINT, solicitar_cierre)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        # En UDP no hay conexion previa: solo se enlaza el puerto de escucha.
        servidor.bind((HOST, PORT))
        # El timeout permite salir del recvfrom() periodicamente para revisar la bandera.
        servidor.settimeout(SOCKET_TIMEOUT)

        print(f"Servidor UDP escuchando en {HOST}:{PORT}")
        print("Pulsa Ctrl+C para detenerlo.")

        try:
            while servidor_activo:
                # recvfrom() devuelve tanto los datos como la direccion del emisor.
                try:
                    datos, direccion = servidor.recvfrom(BUFFER_SIZE)
                except socket.timeout:
                    # Tras cada espera comprobamos si el usuario ha pedido cerrar el servidor.
                    continue
                mensaje = datos.decode("utf-8").strip()
                print(f"Datagrama recibido de {direccion[0]}:{direccion[1]} -> {mensaje}")
        except OSError as error:
            print(f"Error en el servidor UDP: {error}")
        finally:
            print("Servidor UDP detenido.")


if __name__ == "__main__":
    iniciar_servidor()
