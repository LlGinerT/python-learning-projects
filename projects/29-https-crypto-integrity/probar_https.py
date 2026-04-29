"""Cliente de prueba para consumir el endpoint HTTPS del caso práctico."""

import ssl
import urllib.request


URL = "https://127.0.0.1:4443/empleados"


def main() -> None:
    """Realiza una petición HTTPS al servidor local y muestra la respuesta."""
    contexto = ssl._create_unverified_context()

    with urllib.request.urlopen(URL, context=contexto) as respuesta:
        print(f"Codigo: {respuesta.status}")
        print(respuesta.read().decode("utf-8"))


if __name__ == "__main__":
    main()
