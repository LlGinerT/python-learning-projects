"""Cliente UDP secuencial para enviar un datagrama al servidor local."""

import socket


HOST = "127.0.0.1"
PORT = 12346


def main() -> None:
    """Lee un mensaje del usuario y lo envía como datagrama UDP."""
    mensaje = input("Introduce el mensaje Tipo B que quieres enviar: ").strip()

    if not mensaje:
        print("No se ha enviado ningun mensaje porque la entrada esta vacia.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
            # sendto() envia el datagrama directamente sin establecer conexion.
            cliente.sendto(mensaje.encode("utf-8"), (HOST, PORT))
        print("Datagrama enviado correctamente. UDP no espera confirmacion.")
    except OSError as error:
        print(f"Error en el cliente UDP: {error}")


if __name__ == "__main__":
    main()
