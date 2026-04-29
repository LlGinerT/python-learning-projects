"""Herramientas para cifrar y descifrar datos de empleados con AES-GCM."""

import base64
import json
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "datos_empleados.json"
KEY_FILE = BASE_DIR / "clave_aes.bin"
ENCRYPTED_FILE = BASE_DIR / "empleados_cifrados.json"


def cargar_datos() -> list[dict[str, object]]:
    """Carga el listado de empleados desde el archivo JSON original."""
    with DATA_FILE.open("r", encoding="utf-8") as fichero:
        return json.load(fichero)


def cargar_o_crear_clave() -> bytes:
    """Recupera la clave AES guardada o genera una nueva si no existe."""
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()

    clave = AESGCM.generate_key(bit_length=256)
    KEY_FILE.write_bytes(clave)
    return clave


def cifrar_empleados() -> None:
    """Cifra cada empleado y guarda el resultado en un archivo JSON aparte."""
    empleados = cargar_datos()
    clave = cargar_o_crear_clave()
    aes = AESGCM(clave)
    empleados_cifrados = []

    for empleado in empleados:
        nonce = os.urandom(12)
        contenido = json.dumps(empleado, ensure_ascii=False).encode("utf-8")
        cifrado = aes.encrypt(nonce, contenido, None)
        empleados_cifrados.append(
            {
                "nonce": base64.b64encode(nonce).decode("ascii"),
                "datos": base64.b64encode(cifrado).decode("ascii"),
            }
        )

    with ENCRYPTED_FILE.open("w", encoding="utf-8") as fichero:
        json.dump(empleados_cifrados, fichero, indent=2, ensure_ascii=False)

    print(f"Se han cifrado {len(empleados_cifrados)} empleados con AES-GCM.")
    print(f"Archivo generado: {ENCRYPTED_FILE.name}")


def descifrar_empleados() -> None:
    """Descifra los registros almacenados y los muestra por pantalla."""
    if not ENCRYPTED_FILE.exists():
        print("Primero debes ejecutar la opcion de cifrado.")
        return

    clave = cargar_o_crear_clave()
    aes = AESGCM(clave)

    with ENCRYPTED_FILE.open("r", encoding="utf-8") as fichero:
        empleados_cifrados = json.load(fichero)

    print("\nDatos descifrados:")
    for indice, bloque in enumerate(empleados_cifrados, start=1):
        nonce = base64.b64decode(bloque["nonce"])
        cifrado = base64.b64decode(bloque["datos"])
        plano = aes.decrypt(nonce, cifrado, None)
        empleado = json.loads(plano.decode("utf-8"))
        print(f"Empleado {indice}: {empleado}")


def menu() -> None:
    """Presenta las opciones de cifrado hasta que el usuario decide salir."""
    while True:
        print("\nModulo de cifrado AES")
        print("1. Cifrar datos de empleados")
        print("2. Descifrar datos de empleados")
        print("3. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            cifrar_empleados()
        elif opcion == "2":
            descifrar_empleados()
        elif opcion == "3":
            print("Fin del modulo de cifrado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
