# HTTP FTP Inventory API

## What this project does

A small inventory system that combines an FTP upload flow with an HTTP query service.

## What I practiced

- building a basic HTTP server
- uploading files through FTP
- reading CSV inventory data

## How to run it

Install the dependencies first:

```bash
pip install -r requirements.txt
```

Then run the pieces in this order, using separate terminals for the servers:

```bash
python ftp_server_local.py
python upload_inventario.py
python server_inventario.py
python client_consulta.py
```

## Notes

The Spanish `solucion.md` file is an important part of this project. It explains the full flow between FTP upload, HTTP inventory loading and client queries.

The `ftp_root/` folder is the local FTP destination used while testing the upload flow.

The original exercise statement is also included as `enunciado.md`.
