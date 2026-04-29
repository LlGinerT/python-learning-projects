"""Cliente TCP para probar el servidor concurrente basado en hilos."""

import socket


HOST = "127.0.0.1"
PORT = 12355
BUFFER_SIZE = 1024


def enviar_mensaje(mensaje: str) -> None:
    """Envía un mensaje al servidor TCP con hilos y muestra la confirmación."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            # Este cliente sigue siendo secuencial; los hilos estan en el servidor.
            cliente.connect((HOST, PORT))
            cliente.sendall(mensaje.encode("utf-8"))
            confirmacion = cliente.recv(BUFFER_SIZE).decode("utf-8")
            print(f"Confirmacion recibida: {confirmacion}")
    except ConnectionRefusedError:
        print("No ha sido posible conectar con el servidor TCP con hilos.")
    except OSError as error:
        print(f"Error en el cliente TCP: {error}")


def main() -> None:
    """Solicita mensajes por consola hasta que el usuario decida salir."""
    while True:
        mensaje = input("Introduce un mensaje Tipo A (o 'salir' para terminar): ").strip()

        if not mensaje:
            print("Debes introducir un mensaje valido.")
            continue

        if mensaje.lower() == "salir":
            print("Fin del cliente TCP para el servidor con hilos.")
            break

        # Cada envio permite comprobar como responde el servidor concurrente.
        enviar_mensaje(mensaje)


if __name__ == "__main__":
    main()
