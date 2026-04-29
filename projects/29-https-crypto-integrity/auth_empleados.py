"""Utilidades de autenticación local con almacenamiento de hashes SHA-256."""

import hashlib
import json
from pathlib import Path


USERS_FILE = Path(__file__).with_name("usuarios.json")


def cargar_usuarios() -> dict[str, str]:
    """Devuelve los usuarios registrados y sus hashes almacenados."""
    if not USERS_FILE.exists():
        return {}

    with USERS_FILE.open("r", encoding="utf-8") as fichero:
        return json.load(fichero)


def guardar_usuarios(usuarios: dict[str, str]) -> None:
    """Guarda en disco el diccionario de usuarios autenticados."""
    with USERS_FILE.open("w", encoding="utf-8") as fichero:
        json.dump(usuarios, fichero, indent=2, ensure_ascii=False)


def calcular_hash(password: str) -> str:
    """Calcula el hash SHA-256 de una contraseña en texto plano."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def registrar_usuario() -> None:
    """Solicita un nuevo usuario y registra su contraseña en formato hash."""
    usuarios = cargar_usuarios()
    nombre = input("Nuevo nombre de usuario: ").strip()

    if not nombre:
        print("El nombre de usuario no puede estar vacio.")
        return

    if nombre in usuarios:
        print("Ese usuario ya existe.")
        return

    password = input("Contrasena: ").strip()
    if not password:
        print("La contrasena no puede estar vacia.")
        return

    usuarios[nombre] = calcular_hash(password)
    guardar_usuarios(usuarios)
    print("Usuario registrado correctamente. La contrasena se ha almacenado como hash SHA-256.")


def iniciar_sesion() -> None:
    """Comprueba si las credenciales introducidas coinciden con las registradas."""
    usuarios = cargar_usuarios()
    nombre = input("Usuario: ").strip()
    password = input("Contrasena: ").strip()

    hash_introducido = calcular_hash(password)
    hash_guardado = usuarios.get(nombre)

    if hash_guardado is None:
        print("El usuario no existe.")
        return

    if hash_guardado == hash_introducido:
        print("Inicio de sesion valido.")
    else:
        print("Credenciales incorrectas.")


def menu() -> None:
    """Muestra un menú de autenticación hasta que el usuario decide salir."""
    while True:
        print("\nSistema de autenticacion segura")
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Fin del modulo de autenticacion.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
