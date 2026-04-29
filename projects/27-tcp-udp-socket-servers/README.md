# TCP UDP Socket Servers

## What this project does

A client-server networking project with TCP and UDP versions, including threaded and non-threaded implementations.

## What I practiced

- TCP and UDP sockets
- client-server communication
- threaded servers

## How to run it

This project can be tested in four different ways: TCP or UDP, with threads or without threads.

Run each server in one terminal and its matching client in another terminal.

### TCP without threads

```bash
python solucion-sin-hilos/servidor_tcp.py
python solucion-sin-hilos/cliente_tcp.py
```

### UDP without threads

```bash
python solucion-sin-hilos/servidor_udp.py
python solucion-sin-hilos/cliente_udp.py
```

### TCP with threads

```bash
python con-hilos/servidor_tcp_threads.py
python con-hilos/cliente_tcp_threads.py
```

### UDP with threads

```bash
python con-hilos/servidor_udp_threads.py
python con-hilos/cliente_udp_threads.py
```

## Notes

The Spanish `solucion.md` file is an important part of this project. It explains the design decisions, the TCP/UDP behavior and the difference between the threaded and non-threaded versions.

The original exercise statement is also included as `enunciado.md`.
