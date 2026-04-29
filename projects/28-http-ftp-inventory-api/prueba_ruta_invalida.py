"""Script de prueba para comprobar la respuesta ante una ruta HTTP incompleta."""

import requests


def main() -> None:
    """Lanza una petición inválida al servidor y muestra el resultado devuelto."""
    try:
        respuesta = requests.get("http://127.0.0.1:8000/producto", timeout=5)
        print(f"Codigo de estado: {respuesta.status_code}")
        print(f"Respuesta: {respuesta.text}")
    except requests.RequestException as error:
        print(f"No se ha podido realizar la prueba: {error}")


if __name__ == "__main__":
    main()
