"""Cliente TCP secuencial para enviar un único mensaje al servidor local."""

import socket


HOST = "127.0.0.1"
PORT = 12345
BUFFER_SIZE = 1024


def main() -> None:
    """Solicita un mensaje por consola y lo envía al servidor TCP."""
    mensaje = input("Introduce el mensaje Tipo A que quieres enviar: ").strip()

    if not mensaje:
        print("No se ha enviado ningun mensaje porque la entrada esta vacia.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            # connect() establece la conexion antes de enviar el mensaje.
            cliente.connect((HOST, PORT))
            cliente.sendall(mensaje.encode("utf-8"))
            # El cliente espera la confirmacion del servidor para verificar la entrega.
            confirmacion = cliente.recv(BUFFER_SIZE).decode("utf-8")
            print(f"Confirmacion del servidor: {confirmacion}")
    except ConnectionRefusedError:
        print("No ha sido posible conectar con el servidor TCP.")
    except OSError as error:
        print(f"Error en el cliente TCP: {error}")


if __name__ == "__main__":
    main()
