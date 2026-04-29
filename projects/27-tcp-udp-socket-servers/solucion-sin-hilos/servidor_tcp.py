"""Servidor TCP secuencial que confirma la recepción de cada mensaje."""

import signal
import socket


HOST = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024
CONFIRMACION = "Mensaje Tipo A recibido correctamente."
SOCKET_TIMEOUT = 1
# La bandera de estado evita depender de KeyboardInterrupt para salir del bucle.
servidor_activo = True


def solicitar_cierre(signum, frame) -> None:
    """Marca el cierre del servidor cuando el usuario interrumpe la ejecución."""
    del signum, frame
    global servidor_activo
    # Al pulsar Ctrl+C solo pedimos el cierre; no dejamos que aparezca un traceback.
    servidor_activo = False
    print("\nCerrando servidor TCP...")


def iniciar_servidor() -> None:
    """Arranca el servidor TCP y atiende conexiones de forma secuencial."""
    # El manejador de SIGINT transforma Ctrl+C en una parada ordenada.
    signal.signal(signal.SIGINT, solicitar_cierre)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # SO_REUSEADDR evita problemas al reiniciar el servidor rapidamente.
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()
        # accept() no queda bloqueado para siempre y puede revisar la bandera de cierre.
        servidor.settimeout(SOCKET_TIMEOUT)

        print(f"Servidor TCP escuchando en {HOST}:{PORT}")
        print("Pulsa Ctrl+C para detenerlo.")

        try:
            while servidor_activo:
                # accept() bloquea hasta que llega un cliente TCP.
                try:
                    conexion, direccion = servidor.accept()
                except socket.timeout:
                    # Si no llega nadie, el servidor sigue esperando o se cierra si se pulso Ctrl+C.
                    continue
                with conexion:
                    print(f"\nConexion aceptada desde {direccion[0]}:{direccion[1]}")
                    datos = conexion.recv(BUFFER_SIZE)

                    if not datos:
                        print("No se ha recibido ningun contenido.")
                        continue

                    mensaje = datos.decode("utf-8").strip()
                    print(f"Mensaje Tipo A recibido: {mensaje}")
                    # En TCP devolvemos una confirmacion porque el mensaje es critico.
                    conexion.sendall(CONFIRMACION.encode("utf-8"))
        except OSError as error:
            print(f"Error en el servidor TCP: {error}")
        finally:
            print("Servidor TCP detenido.")


if __name__ == "__main__":
    iniciar_servidor()
