# 🧪 Caso Práctico: Desarrollo de una Aplicación Segura para la Gestión de Empleados

---

## 🎯 OBJETIVOS

- Aplicar técnicas de programación segura en el desarrollo de una aplicación para la gestión de empleados, incorporando mecanismos de autenticación robusta.
- Implementar el cifrado y descifrado de datos sensibles, garantizando la protección de información confidencial mediante algoritmos recomendados como AES o Blowfish.
- Configurar un entorno de comunicación segura usando HTTPS con certificado digital, reforzando la transmisión protegida de datos.
- Diseñar e integrar un sistema de verificación de integridad de archivos con algoritmos hash (SHA-256), para detectar posibles alteraciones en la información.
- Documentar de forma clara el proceso de implementación, incluyendo explicaciones y capturas de pantalla que demuestren el funcionamiento de cada módulo de seguridad.

---

## ⏱️ DURACIÓN ESTIMADA

90 minutos.

---

## 📘 ENUNCIADO

Una empresa necesita desarrollar una aplicación básica para la gestión de empleados, pero quiere hacerlo aplicando medidas de seguridad desde el principio.

La aplicación debe cubrir varios aspectos clave de seguridad:

- autenticación segura de usuarios
- cifrado y descifrado de información sensible
- comunicación segura mediante HTTPS
- verificación de integridad de archivos

El objetivo es construir una solución funcional y demostrar, mediante código y documentación, que se han aplicado correctamente los mecanismos de protección.

---

## 🧩 TAREAS A REALIZAR

### 1. Autenticación segura

Implementa un sistema de autenticación para empleados.

Este sistema debe:

- permitir registrar usuarios o definir credenciales de acceso
- evitar almacenar contraseñas en texto plano
- almacenar las contraseñas usando un hash seguro, preferiblemente `SHA-256`
- validar correctamente el inicio de sesión comparando el hash introducido con el almacenado

---

### 2. Cifrado y descifrado de datos

Implementa un módulo que permita proteger información sensible de los empleados.

Este módulo debe:

- cifrar datos utilizando un algoritmo simétrico recomendado:
  - `AES`
  - o `Blowfish`
- permitir posteriormente descifrar esos datos
- demostrar que el proceso de cifrado y descifrado funciona correctamente

Los datos a proteger pueden ser, por ejemplo:

- nombres
- identificadores
- salarios
- información personal básica

---

### 3. Comunicación segura mediante HTTPS

Configura un entorno de comunicación segura para la aplicación.

Debes:

- configurar un servidor accesible por `HTTPS`
- utilizar un certificado digital autofirmado
- demostrar que el acceso seguro funciona desde un navegador o cliente compatible

Además, debes explicar brevemente:

- qué papel cumplen `HTTPS`, `SSL` o `TLS`
- por qué esta configuración mejora la seguridad en la transmisión de datos

---

### 4. Verificación de integridad de archivos

Implementa un mecanismo que permita verificar si un archivo ha sido modificado.

Debes:

- calcular el hash `SHA-256` de uno o varios archivos
- almacenar o mostrar el valor obtenido
- comprobar posteriormente si el archivo ha cambiado
- detectar alteraciones reales comparando los hashes

---

### 5. Documentación

Elabora un documento en formato `Markdown` que explique brevemente cada apartado desarrollado.

Este documento debe incluir:

- explicación del sistema de autenticación
- explicación del cifrado y descifrado
- explicación de la configuración HTTPS
- explicación del sistema de verificación de integridad
- capturas de pantalla que demuestren el funcionamiento de cada parte

---

## ⭐ SE VALORARÁ POSITIVAMENTE

- Que las contraseñas no se almacenen en texto plano y se implementen correctamente con hash seguro (`SHA-256`).
- El uso adecuado de algoritmos de cifrado simétrico recomendados (`AES` o `Blowfish`) tanto para cifrado como para descifrado.
- Una configuración correcta de `HTTPS` con certificado digital autofirmado y su comprobación en navegador.
- La verificación de integridad completa de archivos mediante `SHA-256`, detectando alteraciones reales.

---

## 📊 CRITERIOS DE EVALUACIÓN

### 🔐 Autenticación segura

- **0-40%** → No implementa autenticación o almacena las contraseñas en texto plano.
- **40-70%** → Usa hash, pero con carencias, como algoritmo débil o proceso incompleto.
- **70-100%** → Implementación robusta con `SHA-256` y validación correcta.

---

### 🔒 Cifrado y descifrado

- **0-40%** → No implementa cifrado o usa métodos inseguros.
- **40-70%** → Implementa cifrado simétrico, pero de forma incompleta.
- **70-100%** → Uso correcto de `AES` o `Blowfish`, con cifrado y descifrado funcional.

---

### 🌐 Comunicación segura (HTTPS)

- **0-40%** → No configura `HTTPS` o desconoce `SSL/TLS`.
- **40-70%** → Configura `HTTPS`, pero con errores conceptuales o de implementación.
- **70-100%** → Configuración correcta de `HTTPS` con certificado digital autofirmado y prueba en navegador.

---

### 🧾 Integridad de archivos

- **0-40%** → No aplica verificación de integridad.
- **40-70%** → Explica o usa hash, pero sin demostrar el proceso completo.
- **70-100%** → Verificación correcta de integridad mediante `SHA-256`, detectando alteraciones.

---

### 📝 Documentación y capturas

- **0-40%** → Ausente o incompleta.
- **40-70%** → Explicación parcial y capturas limitadas.
- **70-100%** → Documento bien estructurado, con capturas claras que demuestran funcionamiento.

---

## 📦 ENTREGA

Debes generar:

- Archivos de código fuente para:
  - autenticación
  - cifrado y descifrado
  - verificación de integridad

- La configuración necesaria del servidor `HTTPS` y el certificado utilizado.

- Un archivo `solucion.md` que incluya:
  - explicación breve de cada apartado
  - capturas de pantalla que demuestren el funcionamiento de:
    - registro o login
    - cifrado y descifrado
    - acceso por HTTPS
    - verificación de integridad

⚠️ No es necesario generar archivos ZIP ni PDF.  
Todo debe entregarse en formato `.md`, archivos de código fuente y los recursos necesarios para la configuración segura.
