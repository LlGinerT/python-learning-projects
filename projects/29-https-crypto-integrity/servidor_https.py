"""Servidor HTTPS que publica un portal seguro y un listado de empleados."""

import json
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


HOST = "127.0.0.1"
PORT = 4443
BASE_DIR = Path(__file__).resolve().parent
CERT_FILE = BASE_DIR / "certs" / "cert.pem"
KEY_FILE = BASE_DIR / "certs" / "key.pem"
DATA_FILE = BASE_DIR / "datos_empleados.json"


def cargar_empleados() -> list[dict[str, object]]:
    """Carga en memoria los datos de empleados que se servirán por HTTPS."""
    with DATA_FILE.open("r", encoding="utf-8") as fichero:
        return json.load(fichero)


class SecureHandler(BaseHTTPRequestHandler):
    """Manejador HTTP seguro para servir la página principal y el JSON."""
    empleados = cargar_empleados()

    def _responder(self, codigo: int, contenido: bytes, content_type: str) -> None:
        """Envía una respuesta HTTP con el contenido y cabeceras indicados."""
        self.send_response(codigo)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(contenido)))
        self.end_headers()
        self.wfile.write(contenido)

    def do_GET(self) -> None:
        """Atiende las rutas ``/`` y ``/empleados`` del servidor HTTPS."""
        if self.path == "/":
            html = """
            <html lang="es">
                <head><meta charset="utf-8"><title>Portal seguro de empleados</title></head>
                <body>
                    <h1>Portal seguro de empleados</h1>
                    <p>La comunicacion se esta realizando mediante HTTPS.</p>
                    <p>Consulta los datos en <code>/empleados</code>.</p>
                </body>
            </html>
            """.strip().encode("utf-8")
            self._responder(200, html, "text/html; charset=utf-8")
            return

        if self.path == "/empleados":
            contenido = json.dumps(self.empleados, ensure_ascii=False, indent=2).encode("utf-8")
            self._responder(200, contenido, "application/json; charset=utf-8")
            return

        self._responder(404, b"Recurso no encontrado.", "text/plain; charset=utf-8")

    def log_message(self, format: str, *args: object) -> None:
        """Personaliza el formato de log para las peticiones recibidas."""
        print(f"[HTTPS] {self.address_string()} - {format % args}")


def main() -> None:
    """Configura TLS y arranca el servidor HTTPS hasta su detención manual."""
    if not CERT_FILE.exists() or not KEY_FILE.exists():
        print("Faltan el certificado o la clave privada en la carpeta certs.")
        return

    servidor = HTTPServer((HOST, PORT), SecureHandler)
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    contexto.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    servidor.socket = contexto.wrap_socket(servidor.socket, server_side=True)

    print(f"Servidor HTTPS disponible en https://{HOST}:{PORT}")
    print("Pulsa Ctrl+C para detenerlo.")

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor HTTPS detenido por el usuario.")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
