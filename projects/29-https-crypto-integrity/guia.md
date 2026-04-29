# GUÍA PARA LA RESOLUCIÓN DEL CASO PRÁCTICO:

“Desarrollo de una Aplicación Segura para la Gestión de Empleados”

## Enfoque de evaluación del caso práctico:

El caso práctico debe orientarse a demostrar que cada requisito de seguridad queda implementado, comprobado y documentado de forma trazable. El análisis debe separar los cuatro bloques exigidos en el enunciado: autenticación, cifrado de datos sensibles, comunicación segura e integridad de archivos, relacionándolos con sus evidencias de funcionamiento. El temario de la UD05 refuerza esta lógica al vincular las funciones hash con credenciales e integridad, los algoritmos simétricos con protección de información y HTTPS con SSL/TLS y certificado digital.

Conviene priorizar pruebas como: almacenamiento de contraseñas como hash SHA-256, validación de acceso comparando resúmenes, cifrado y posterior descifrado de un dato sensible, acceso a la aplicación por HTTPS con certificado autofirmado visible en navegador, y verificación de integridad detectando cambios en un informe generado.

---

## Herramientas y recursos necesarios para llevar a cabo la práctica:

- Temario de la UD05 sobre hash, cifrado simétrico, SSL/TLS y HTTPS.

- Entorno de desarrollo del lenguaje elegido para crear el prototipo. Opción habitual: Visual Studio Code  
  https://code.visualstudio.com/

Programación de Servicios y Procesos | Unidad 5

- Librería criptográfica compatible con cifrado simétrico, para proteger datos sensibles. Opción habitual en Python:  
  cryptography https://cryptography.io/

---

## Tiempo estimado de realización:

La estimación de tiempo para la resolución de esta actividad es de 180 minutos, pero se debe tener en cuenta que en el caso de tener que instalar software, realizar búsquedas de recursos necesarios o hacer configuraciones este tiempo puede aumentar.

Recuerda, siempre son estimaciones ya que se suman, además, factores como el rendimiento de tu equipo o la conexión a internet.

---

## Estrategia de análisis y resolución:

1. Extraer del enunciado los requisitos fijos y convertirlos en una lista de comprobación: qué debe almacenarse, qué debe cifrarse, qué debe servirse por HTTPS y qué evidencia habrá que entregar.

2. Dividir la práctica en módulos independientes para evitar retrabajo:
   - autenticación
   - protección de datos sensibles
   - servidor seguro
   - integridad del informe

3. Diseñar primero la lógica de autenticación: registro, generación del hash SHA-256 y validación comparando el resumen introducido con el almacenado, sin conservar contraseñas en texto plano.

4. Integrar después el tratamiento del dato sensible: definir qué campo se cifra, aplicar un algoritmo simétrico recomendado y comprobar que puede recuperarse correctamente al consultar el empleado. El objetivo es demostrar confidencialidad y uso funcional del descifrado.

Programación de Servicios y Procesos | Unidad 5

5. Montar el acceso HTTPS sobre la aplicación, generar e instalar el certificado autofirmado y verificar desde navegador que la conexión utiliza canal seguro aunque exista advertencia por confianza del certificado.

6. Generar el informe final de empleados, calcular su hash SHA-256, guardar el valor asociado y repetir el cálculo tras una modificación de prueba para contrastar coincidencia o alteración.

---

## Elementos diferenciales para optar a mayor calificación:

- La planificación refleja una correspondencia completa entre requisitos del enunciado, módulos implementados y evidencias aportadas.
- La autenticación demuestra que la validación se basa en comparación de hash SHA-256 y no en contraseñas legibles.
- El tratamiento del dato sensible evidencia separación correcta entre almacenamiento cifrado y visualización mediante descifrado funcional.
- La configuración HTTPS demuestra uso real de canal seguro con certificado digital instalado y comprobación en navegador.
- La verificación de integridad demuestra comparación efectiva entre hash original y hash recalculado ante posibles alteraciones
