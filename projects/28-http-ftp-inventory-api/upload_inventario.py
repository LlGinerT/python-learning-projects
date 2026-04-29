"""Cliente FTP que sube el inventario CSV al directorio remoto compartido."""

from ftplib import FTP, all_errors
from pathlib import Path


HOST = "127.0.0.1"
PORT = 2121
USER = "admin"
PASSWORD = "admin123"
REMOTE_DIR = "/inventario"
LOCAL_FILE = Path(__file__).with_name("productos.csv")


def subir_archivo() -> None:
    """Sube el CSV local al directorio remoto que luego leera el servidor HTTP."""
    if not LOCAL_FILE.exists():
        print(f"No se encuentra el archivo local: {LOCAL_FILE}")
        return

    ftp = FTP()

    try:
        print(f"Conectando con el servidor FTP {HOST}:{PORT}...")
        ftp.connect(HOST, PORT, timeout=10)
        ftp.login(USER, PASSWORD)
        print("Conexion FTP establecida correctamente.")

        # El servidor HTTP leera el archivo desde este directorio compartido.
        ftp.cwd(REMOTE_DIR)

        with LOCAL_FILE.open("rb") as fichero:
            ftp.storbinary(f"STOR {LOCAL_FILE.name}", fichero)

        print(f"Archivo {LOCAL_FILE.name} subido correctamente a {REMOTE_DIR}.")
        print("El inventario ya esta disponible para que lo cargue el servidor HTTP.")
    except all_errors as error:
        print(f"Error durante la transferencia FTP: {error}")
    finally:
        try:
            ftp.quit()
            print("Sesion FTP cerrada con quit().")
        except all_errors:
            ftp.close()
            print("Conexion FTP cerrada con close().")


if __name__ == "__main__":
    subir_archivo()
