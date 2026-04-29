"""Servidor FTP local usado para depositar el CSV del inventario de la práctica."""

from pathlib import Path

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


HOST = "127.0.0.1"
PORT = 2121
USER = "admin"
PASSWORD = "admin123"
BASE_DIR = Path(__file__).resolve().parent
FTP_ROOT = BASE_DIR / "ftp_root"
INVENTARIO_DIR = FTP_ROOT / "inventario"


def main() -> None:
    """Arranca un servidor FTP local para probar la práctica completa."""
    INVENTARIO_DIR.mkdir(parents=True, exist_ok=True)

    authorizer = DummyAuthorizer()
    authorizer.add_user(USER, PASSWORD, str(FTP_ROOT), perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer

    servidor = FTPServer((HOST, PORT), handler)
    print(f"Servidor FTP escuchando en {HOST}:{PORT}")
    print(f"Directorio raiz FTP: {FTP_ROOT}")
    print("Sube el CSV a la carpeta remota /inventario")
    print("Pulsa Ctrl+C para detenerlo.")

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor FTP detenido por el usuario.")
    finally:
        servidor.close_all()


if __name__ == "__main__":
    main()
