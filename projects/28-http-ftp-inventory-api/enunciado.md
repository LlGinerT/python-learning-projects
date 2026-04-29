# 🧪 Caso Práctico: Sistema Básico de Gestión de Inventario para PYMES

---

## 🎯 OBJETIVOS

- Descubrir y aplicar los protocolos de red utilizados para implementar servicios populares, específicamente HTTP y FTP.
- Conocer y utilizar algunas de las librerías más habituales de Python relacionadas con protocolos de Internet.
- Aprender a desarrollar un servidor HTTP básico que proporcione servicios web y clientes que lo consuman.
- Comprender y aplicar los conceptos de establecimiento y finalización de conexiones para liberar recursos.
- Demostrar la transmisión de información utilizando protocolos de aplicación.

---

## ⏱️ DURACIÓN ESTIMADA

90 minutos.

---

## 📘 ENUNCIADO

Una pequeña empresa de venta de componentes electrónicos necesita un sistema sencillo para gestionar su inventario. Actualmente, los datos de los productos se almacenan en archivos CSV, y la información debe estar accesible para que los vendedores puedan consultarla rápidamente y para que los administradores puedan actualizarla.

Se requiere desarrollar tres componentes principales para este sistema:

- **Un script de carga de inventario:** permitirá a los administradores subir archivos CSV con nuevos datos de productos al servidor central para su procesamiento.
- **Un servicio web de consulta de productos:** expondrá una API sencilla para que los vendedores puedan consultar el stock y la descripción de un producto dado su ID.
- **Un cliente de consulta:** será una aplicación de consola que permita a los vendedores interactuar con el servicio web para obtener información de productos de forma interactiva.

---

## 🧩 TAREAS A REALIZAR

### 1. Preparación del entorno

Crea un archivo CSV de ejemplo llamado `productos.csv` con un contenido similar a este:

```csv
ID,Nombre,Descripcion,Stock
P001,Teclado Mecánico,Teclado de alta calidad para gaming,150
P002,Ratón Óptico,Ratón ergonómico con sensor preciso,200
P003,Monitor Curvo,Monitor de 27 pulgadas 144Hz,75
```

Además:

- Asegúrate de tener un servidor FTP accesible. Puede ser un servidor FTP real o una simulación local, aunque para obtener la máxima puntuación se espera interacción con un servidor FTP real.
- Asegúrate de tener Python y `pip` instalados.
- Instala la librería `requests` si aún no la tienes.

---

## 2. Desarrollo del cliente FTP para carga de datos (`upload_inventario.py`)

Crea un script en Python que utilice la librería `ftplib` para conectarse a un servidor FTP.

Este script debe:

- Permitir autenticación si el servidor la requiere.
- Subir el archivo `productos.csv` desde la máquina local a una ubicación concreta del servidor FTP.
- Establecer y cerrar correctamente la conexión FTP al finalizar la transferencia.
- Liberar correctamente los recursos asociados a la conexión.

---

## 3. Desarrollo del servicio web de consulta (`server_inventario.py`)

Crea un servidor HTTP básico en Python.

Este servidor debe:

- Escuchar peticiones HTTP en el puerto `8000`.
- Cargar al inicio los datos del archivo `productos.csv` en una estructura en memoria, por ejemplo un diccionario.
- Atender peticiones `GET` a la ruta:

```text
/producto/<id_producto>
```

## Comportamiento esperado

- Si el producto existe:
  - devolver los datos en formato JSON
  - responder con código `200`

- Si el producto no existe:
  - devolver un mensaje JSON indicando que no fue encontrado
  - responder con código `404`

- Si la ruta no tiene el formato correcto:
  - responder con código `400`

---

Debes construir la respuesta usando los métodos:

- `send_response`
- `send_header`
- `end_headers`
- `wfile.write`

El servidor debe permanecer en ejecución esperando peticiones mediante `serve_forever()`.

---

## 4. Desarrollo del cliente de consulta (`client_consulta.py`)

Crea un script en Python que actúe como cliente del servicio HTTP anterior.

Este script debe:

- Pedir al usuario el ID del producto a consultar.
- Realizar una petición HTTP GET al servidor, por ejemplo:

```text
http://localhost:8000/producto/P001
```

- Usar la librería `requests` para hacer la consulta.

---

### Gestión de respuestas

- Si el código de estado es `200`:
  - mostrar la información del producto de forma legible

- Si el código de estado es `404`:
  - indicar que el producto no fue encontrado

- Para otros errores (`400`, `500`, etc.):
  - mostrar un mensaje genérico de error

---

Además:

- debe permitir múltiples consultas hasta que el usuario decida salir

---

## ⭐ SE VALORARÁ POSITIVAMENTE

- Inclusión de comentarios claros y concisos en el código.
- Manejo adecuado de errores y excepciones en todos los scripts.
- Organización del código en funciones o clases para mejorar la legibilidad y el mantenimiento.
- Demostración de comprensión sobre el establecimiento y cierre de conexiones y la liberación de recursos asociados.

---

## 📊 CRITERIOS DE EVALUACIÓN

### 📤 Cliente FTP

- 0-20% → No funciona o no existe.
- 20-40% → Conecta al servidor FTP, pero la subida falla.
- 40-60% → Sube el archivo, pero la gestión de la conexión es incompleta.
- 60-80% → Sube el archivo correctamente y las conexiones se manejan adecuadamente.
- 80-100% → Sube el archivo de forma robusta, con manejo de errores y cierre explícito de conexiones (`quit` / `close`).

---

### 🌐 Servidor HTTP

- 0-20% → No funciona o no existe.
- 20-40% → Arranca, pero no responde a peticiones o las maneja incorrectamente.
- 40-60% → Responde a peticiones `GET` básicas, pero la gestión de cabeceras es limitada.
- 60-80% → Responde correctamente a peticiones `GET` para productos existentes y maneja `404` para no existentes.
- 80-100% → Implementa el servidor HTTP con gestión de códigos de estado (`200`, `400`, `404`), devuelve JSON válido y carga los datos del CSV.

---

### 🖥️ Cliente HTTP

- 0-20% → No funciona o no existe.
- 20-40% → Realiza peticiones, pero no procesa la respuesta adecuadamente.
- 40-60% → Procesa respuestas `200` y muestra datos, pero sin manejo de errores.
- 60-80% → Procesa respuestas `200` y `404`, mostrando la información o el error según corresponda.
- 80-100% → Interacciona correctamente con el servidor, maneja códigos de estado (`200`, `404`, otros errores) y muestra la información de forma clara, permitiendo múltiples consultas.

---

### 📚 Uso de librerías

- 0-20% → No utiliza librerías o las usa incorrectamente.
- 20-40% → Uso mínimo y/o incorrecto de `ftplib` o `http.server`.
- 40-60% → Uso básico de las librerías, pero sin aprovechar sus funcionalidades.
- 60-80% → Utiliza las librerías principales (`ftplib`, `http.server`, `requests`) de forma funcional.
- 80-100% → Utiliza las librerías adecuadas de Python de forma eficiente e idiomática, demostrando comprensión avanzada.

---

### 🧩 Código y estructura

- 0-20% → Código desorganizado; no sigue buenas prácticas.
- 20-40% → Código funcional, pero con poca modularidad o pocos comentarios.
- 40-60% → Código estructurado y legible, con comentarios básicos.
- 60-80% → Código bien estructurado, legible, con manejo de errores básico y comentarios pertinentes.
- 80-100% → Código limpio, modular, bien documentado, con manejo de excepciones y validaciones, siguiendo buenas prácticas de programación.

---

## 📦 ENTREGA

Debes generar:

- `upload_inventario.py`
- `server_inventario.py`
- `client_consulta.py`
- `productos.csv`

Además, debe generarse un archivo `solucion.md` que incluya:

- una breve explicación de cómo configurar y arrancar el servidor FTP, si aplica
- cómo ejecutar cada uno de los scripts Python
- cualquier instrucción especial o prerrequisito para la ejecución
- capturas de pantalla que demuestren:
  - la ejecución del cliente FTP subiendo el archivo
  - el servidor HTTP arrancado y respondiendo
  - la interacción del cliente HTTP consultando un producto existente y un producto no existente

⚠️ No es necesario generar archivos ZIP ni PDF.  
Todo debe entregarse en formato `.md`, `.py` y `.csv`.
