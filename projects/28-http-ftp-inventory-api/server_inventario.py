"""Servidor HTTP que expone por API los productos cargados desde un CSV."""

import csv
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse


HOST = "127.0.0.1"
PORT = 8000
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "ftp_root" / "inventario" / "productos.csv"


def cargar_productos() -> dict[str, dict[str, object]]:
    """Carga en memoria el CSV que previamente se ha subido al FTP."""
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            "No se ha encontrado el inventario subido por FTP. "
            "Ejecuta antes upload_inventario.py."
        )

    inventario: dict[str, dict[str, object]] = {}

    with CSV_PATH.open("r", encoding="utf-8", newline="") as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            producto_id = fila["ID"].strip().upper()
            inventario[producto_id] = {
                "id": producto_id,
                "nombre": fila["Nombre"].strip(),
                "descripcion": fila["Descripcion"].strip(),
                "stock": int(fila["Stock"]),
            }

    return inventario


class InventarioHandler(BaseHTTPRequestHandler):
    """Manejador HTTP encargado de servir consultas individuales de productos."""
    inventario: dict[str, dict[str, object]] = {}

    def _responder_json(self, codigo: int, payload: dict[str, object]) -> None:
        """Envía una respuesta JSON con el código HTTP indicado."""
        contenido = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(contenido)))
        self.end_headers()
        self.wfile.write(contenido)

    def do_GET(self) -> None:
        """Procesa peticiones GET del tipo ``/producto/<id_producto>``."""
        ruta = urlparse(self.path).path.strip("/")
        partes = ruta.split("/")

        if len(partes) != 2 or partes[0] != "producto" or not partes[1]:
            self._responder_json(400, {"error": "La ruta debe tener el formato /producto/<id_producto>."})
            return

        producto_id = partes[1].upper()
        producto = self.inventario.get(producto_id)

        if producto is None:
            self._responder_json(404, {"error": f"El producto {producto_id} no existe."})
            return

        self._responder_json(200, producto)

    def log_message(self, format: str, *args: object) -> None:
        """Redirige el log HTTP a la salida estándar con un formato legible."""
        print(f"[HTTP] {self.address_string()} - {format % args}")


def main() -> None:
    """Carga el inventario y deja el servidor HTTP escuchando hasta su cierre."""
    try:
        InventarioHandler.inventario = cargar_productos()
    except (FileNotFoundError, OSError, ValueError, KeyError) as error:
        print(f"No se ha podido iniciar el servidor HTTP: {error}")
        return

    servidor = HTTPServer((HOST, PORT), InventarioHandler)
    print(f"Inventario cargado desde {CSV_PATH}.")
    print(f"Productos disponibles en memoria: {len(InventarioHandler.inventario)}")
    print(f"Servidor HTTP escuchando en http://{HOST}:{PORT}")
    print("Pulsa Ctrl+C para detenerlo.")

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor HTTP detenido por el usuario.")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
