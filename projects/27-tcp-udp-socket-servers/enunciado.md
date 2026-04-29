# 🧪 Caso Práctico: Sistema de Comunicación Cliente-Servidor Híbrido con Sockets en Python

---

## 🎯 OBJETIVOS

- Implementar un sistema de comunicación basado en el modelo cliente-servidor utilizando sockets.
- Diferenciar y aplicar los tipos de sockets orientados a conexión y no orientados a conexión.
- Utilizar los protocolos TCP y UDP comprendiendo sus características y casos de uso.
- Configurar y usar las funciones básicas de programación de sockets en Python para la transmisión y recepción de información entre procesos.
- Analizar las diferencias entre comunicaciones fiables (TCP) y comunicaciones orientadas a velocidad (UDP).

---

## ⏱️ DURACIÓN ESTIMADA

90 minutos.

---

## 📘 ENUNCIADO

Una pequeña empresa necesita implementar un sistema de comunicación interno básico para su personal, que combine fiabilidad y rapidez.

El sistema debe permitir dos tipos de mensajes:

- **Mensajes urgentes y confirmados (Tipo A):** son críticos, requieren confirmación de entrega y deben llegar sin errores y en orden. Se usan, por ejemplo, para asignar tareas importantes a un usuario concreto.
- **Mensajes de anuncio rápido (Tipo B):** son menos críticos, como avisos generales o actualizaciones de estado, donde la velocidad es prioritaria sobre la garantía de entrega o el orden. No requieren confirmación de recepción.

Para ello, se solicita desarrollar un servidor central y dos tipos de clientes, uno para cada tipo de mensaje, utilizando Python y sockets.

---

## 🧩 TAREAS A REALIZAR

### 1. Desarrollo del servidor TCP

Crea un servidor en Python que utilice un socket orientado a conexión (**TCP**).

Este servidor debe:

- Escuchar en `localhost` (`127.0.0.1`) y un puerto específico, por ejemplo `12345`.
- Aceptar conexiones de clientes.
- Recibir un mensaje de texto de Tipo A.
- Procesar el mensaje, por ejemplo mostrándolo por consola.
- Enviar una confirmación al cliente indicando que el mensaje fue recibido correctamente.

Además:

- Debe poder gestionar múltiples conexiones de clientes de forma consecutiva.
- No es obligatorio usar hilos en esta versión básica.

---

### 2. Desarrollo del cliente TCP

Crea un cliente en Python que utilice un socket orientado a conexión (**TCP**).

Este cliente debe:

- Conectarse al servidor TCP en la dirección y puerto indicados.
- Permitir al usuario introducir un mensaje de Tipo A.
- Enviar el mensaje al servidor.
- Esperar la confirmación del servidor.
- Mostrar la confirmación recibida por pantalla.

---

### 3. Desarrollo del servidor UDP

Crea un servidor en Python que utilice un socket no orientado a conexión (**UDP**).

Este servidor debe:

- Escuchar en `localhost` (`127.0.0.1`) y un puerto diferente al del servidor TCP, por ejemplo `12346`.
- Recibir datagramas de clientes con mensajes de Tipo B.
- Procesar esos mensajes, por ejemplo mostrándolos por consola.

Además:

- No debe enviar ninguna confirmación al cliente.

---

### 4. Desarrollo del cliente UDP

Crea un cliente en Python que utilice un socket no orientado a conexión (**UDP**).

Este cliente debe:

- Enviar datagramas con mensajes de Tipo B al servidor UDP.
- Permitir al usuario introducir un mensaje.
- Enviar el mensaje al servidor.
- No esperar ninguna respuesta ni confirmación.

---

### 5. Documentación y justificación

Debes elaborar una explicación que incluya:

- Una descripción breve de cada archivo de código.
- La justificación de por qué se usa **TCP** para los mensajes urgentes y confirmados.
- La justificación de por qué se usa **UDP** para los mensajes de anuncio rápido.
- Una comparación entre ambos protocolos en términos de:
  - fiabilidad
  - orden
  - confirmación
  - velocidad
  - casos de uso

También deben incluirse capturas de pantalla que demuestren la ejecución correcta de ambos sistemas.

---

## ⭐ SE VALORARÁ POSITIVAMENTE

- Manejo de excepciones mediante `try-except` en clientes y servidores.
- Capacidad de comunicación entre distintos sistemas operativos.
- Uso de hilos (`threads`) en el servidor TCP para atender varios clientes de forma concurrente.
- Presentación clara y concisa de resultados y conclusiones.

---

## 📊 CRITERIOS DE EVALUACIÓN

### 🔌 Implementación servidor/cliente TCP

- **0-20% (Insuficiente):** No funciona o presenta errores graves en el diseño del socket y la comunicación.
- **20-40% (Necesita mejorar):** Funcionalidad básica pero con errores significativos en la conexión o en el intercambio de datos.
- **40-60% (Aceptable):** Funciona, pero con manejo de errores básico o con pequeños fallos intermitentes.
- **60-80% (Bueno):** Completamente funcional, logra el intercambio de mensajes y confirmación de forma fiable.
- **80-100% (Excelente):** Completamente funcional y robusto, con manejo adecuado de excepciones y cierres de conexión.

---

### 📡 Implementación servidor/cliente UDP

- **0-20% (Insuficiente):** No funciona o presenta errores graves en el diseño del socket y la comunicación.
- **20-40% (Necesita mejorar):** Funcionalidad básica pero con errores significativos en el envío o recepción de datagramas.
- **40-60% (Aceptable):** Funciona, pero con manejo de errores básico o con pequeños fallos intermitentes.
- **60-80% (Bueno):** Completamente funcional, logra el intercambio de datagramas de forma eficiente.
- **80-100% (Excelente):** Completamente funcional y robusto, con un uso óptimo del protocolo UDP.

---

### 💻 Calidad del código

- **0-20% (Insuficiente):** Código desorganizado, sin comentarios, difícil de entender o con graves errores de sintaxis o lógica.
- **20-40% (Necesita mejorar):** Código con estructura pobre, pocos comentarios y algunos errores lógicos o de estilo.
- **40-60% (Aceptable):** Código legible, con estructura clara y comentarios adecuados en partes clave, pero con pocos errores.
- **60-80% (Bueno):** Código claro, bien estructurado y documentado, siguiendo buenas prácticas de programación.
- **80-100% (Excelente):** Código óptimo, modular, extensible, con manejo de errores y excelente documentación interna mediante comentarios.

---

### 🧠 Justificación y documentación

- **0-20% (Insuficiente):** Ausente o muy pobre, sin explicación de decisiones.
- **20-40% (Necesita mejorar):** Documentación breve y poco clara, con justificación mínima o incorrecta.
- **40-60% (Aceptable):** Aceptable, explica el funcionamiento básico y la elección de protocolos.
- **60-80% (Bueno):** Detallada y clara, explica el funcionamiento, justifica decisiones y muestra pruebas.
- **80-100% (Excelente):** Completa y concisa, con justificaciones técnicas sólidas y capturas de pantalla que validan la solución.

---

### 🔗 Uso de sockets y protocolos

- **0-20% (Insuficiente):** Uso incorrecto de los tipos de sockets o desconocimiento de los protocolos asociados.
- **20-40% (Necesita mejorar):** Uso parcial de sockets, con confusión en la aplicación de TCP/UDP o sus características.
- **40-60% (Aceptable):** Uso correcto de sockets, con distinción clara entre TCP y UDP, pero sin profundidad en la justificación.
- **60-80% (Bueno):** Aplicación efectiva de sockets y uso justificado de los protocolos adecuados según los requisitos.
- **80-100% (Excelente):** Aplicación óptima de sockets y justificación profunda de la elección de TCP y UDP, demostrando comprensión de sus características clave.

---

## 📦 ENTREGA

Debes generar:

### Versión básica sin hilos

- `servidor_tcp.py`
- `cliente_tcp.py`
- `servidor_udp.py`
- `cliente_udp.py`

### Versión ampliada con hilos

- `servidor_tcp_threads.py`
- `cliente_tcp_threads.py`
- `servidor_udp_threads.py`
- `cliente_udp_threads.py`

### Documentación

- Un archivo `solucion.md` que incluya:
  - una descripción breve de cada archivo de código
  - la justificación detallada de por qué se eligió TCP para los mensajes urgentes y confirmados
  - la justificación detallada de por qué se eligió UDP para los mensajes de anuncio rápido
  - capturas de pantalla que demuestren la ejecución correcta de los programas y la comunicación entre ellos
  - cualquier otra consideración o aprendizaje relevante

⚠️ No es necesario generar archivos ZIP ni PDF.  
Todo debe entregarse en formato `.md` y `.py`.
