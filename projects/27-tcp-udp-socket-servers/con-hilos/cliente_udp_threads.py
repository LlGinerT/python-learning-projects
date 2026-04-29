"""Cliente UDP para enviar datagramas al servidor concurrente con hilos."""

import socket


HOST = "127.0.0.1"
PORT = 12356


def enviar_datagrama(mensaje: str) -> None:
    """Envía un datagrama UDP al servidor local de la práctica."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
            # El cliente solo envia; la concurrencia se observa en el servidor UDP con hilos.
            cliente.sendto(mensaje.encode("utf-8"), (HOST, PORT))
        print(f"Datagrama enviado: {mensaje}")
    except OSError as error:
        print(f"Error en el cliente UDP: {error}")


def main() -> None:
    """Mantiene una sesión interactiva de envío de datagramas por UDP."""
    while True:
        mensaje = input("Introduce un mensaje Tipo B (o 'salir' para terminar): ").strip()

        if not mensaje:
            print("Debes introducir un mensaje valido.")
            continue

        if mensaje.lower() == "salir":
            print("Fin del cliente UDP para el servidor con hilos.")
            break

        enviar_datagrama(mensaje)


if __name__ == "__main__":
    main()
