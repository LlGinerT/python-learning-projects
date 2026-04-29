# HTTPS Crypto Integrity

## What this project does

A security-focused project with employee data encryption, file integrity checks and a small HTTPS server.

## What I practiced

- AES-GCM encryption
- hashing files for integrity
- serving HTTPS locally

## How to run it

Install the dependencies first:

```bash
pip install -r requirements.txt
```

Then run the parts you want to test:

```bash
python cifrado_empleados.py
python integridad_archivos.py
python servidor_https.py
```

## Notes

The `certs/` folder contains local practice certificates for running the HTTPS server.

The Spanish `solucion.md` file is an important part of this project. It explains how the authentication, encryption, integrity checks and HTTPS server fit together.

The original exercise statement is also included as `enunciado.md`.
