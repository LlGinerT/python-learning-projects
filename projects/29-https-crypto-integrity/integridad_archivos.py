"""Comprobación de integridad de archivos mediante hashes SHA-256."""

import hashlib
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
HASHES_FILE = BASE_DIR / "hashes.json"


def calcular_sha256(ruta: Path) -> str:
    """Calcula el resumen SHA-256 del archivo indicado."""
    resumen = hashlib.sha256()

    with ruta.open("rb") as fichero:
        for bloque in iter(lambda: fichero.read(4096), b""):
            resumen.update(bloque)

    return resumen.hexdigest()


def cargar_hashes() -> dict[str, str]:
    """Carga del disco los hashes previamente registrados."""
    if not HASHES_FILE.exists():
        return {}

    with HASHES_FILE.open("r", encoding="utf-8") as fichero:
        return json.load(fichero)


def guardar_hashes(datos: dict[str, str]) -> None:
    """Persiste en JSON los hashes registrados por el usuario."""
    with HASHES_FILE.open("w", encoding="utf-8") as fichero:
        json.dump(datos, fichero, indent=2, ensure_ascii=False)


def registrar_archivo() -> None:
    """Registra el hash actual de un archivo existente en la carpeta base."""
    nombre = input("Nombre del archivo que quieres registrar: ").strip()
    ruta = BASE_DIR / nombre

    if not ruta.exists() or not ruta.is_file():
        print("El archivo indicado no existe.")
        return

    hashes = cargar_hashes()
    hashes[nombre] = calcular_sha256(ruta)
    guardar_hashes(hashes)

    print(f"Hash SHA-256 registrado para {nombre}.")
    print(hashes[nombre])


def verificar_archivo() -> None:
    """Compara el hash actual de un archivo con el hash almacenado."""
    nombre = input("Nombre del archivo que quieres verificar: ").strip()
    ruta = BASE_DIR / nombre
    hashes = cargar_hashes()
    hash_guardado = hashes.get(nombre)

    if hash_guardado is None:
        print("Ese archivo no tiene un hash registrado.")
        return

    if not ruta.exists() or not ruta.is_file():
        print("El archivo indicado no existe actualmente.")
        return

    hash_actual = calcular_sha256(ruta)
    print(f"Hash guardado: {hash_guardado}")
    print(f"Hash actual:   {hash_actual}")

    if hash_guardado == hash_actual:
        print("La integridad es correcta. El archivo no ha cambiado.")
    else:
        print("Se ha detectado una alteracion en el archivo.")


def menu() -> None:
    """Muestra el menú principal del módulo de verificación de integridad."""
    while True:
        print("\nVerificacion de integridad")
        print("1. Registrar hash de un archivo")
        print("2. Verificar integridad de un archivo")
        print("3. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            registrar_archivo()
        elif opcion == "2":
            verificar_archivo()
        elif opcion == "3":
            print("Fin del modulo de integridad.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
