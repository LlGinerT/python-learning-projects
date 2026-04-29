"""Cliente HTTP para consultar productos del inventario publicado por el servidor."""

import requests


BASE_URL = "http://127.0.0.1:8000/producto/{}"


def consultar_producto(producto_id: str) -> None:
    """Consulta un producto por su identificador y muestra la respuesta recibida."""
    try:
        # La consulta HTTP siempre se realiza contra el servidor local del caso practico.
        respuesta = requests.get(BASE_URL.format(producto_id), timeout=5)
    except requests.RequestException as error:
        print(f"No se ha podido completar la consulta HTTP: {error}")
        return

    if respuesta.status_code == 200:
        datos = respuesta.json()
        print("\nProducto encontrado:")
        print(f"ID: {datos['id']}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Descripcion: {datos['descripcion']}")
        print(f"Stock: {datos['stock']}")
    elif respuesta.status_code == 404:
        datos = respuesta.json()
        print(f"\nAviso: {datos['error']}")
    else:
        print(f"\nSe ha producido un error HTTP ({respuesta.status_code}).")
        try:
            print(respuesta.json())
        except ValueError:
            print(respuesta.text)


def main() -> None:
    """Mantiene una sesión interactiva de consultas hasta que el usuario sale."""
    print("Consulta interactiva del inventario. Escribe 'salir' para terminar.")

    while True:
        producto_id = input("\nIntroduce el ID del producto: ").strip()

        if not producto_id:
            print("Debes introducir un ID valido.")
            continue

        if producto_id.lower() == "salir":
            print("Fin del cliente de consulta.")
            break

        consultar_producto(producto_id.upper())


if __name__ == "__main__":
    main()
