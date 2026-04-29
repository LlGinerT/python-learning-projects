# 🧪 Caso Práctico: Procesamiento de Datos con Monohilo, Multihilo y Multiproceso

---

## 🎯 OBJETIVOS

- Aprender a identificar el concepto de proceso y su relación con los programas informáticos.
- Comprender las diferencias entre procesos y servicios.
- Identificar el ciclo de vida de los procesos y su gestión por el sistema operativo.
- Entender el concepto de hilos de ejecución y su diferencia respecto a los procesos.
- Conocer los sistemas multitarea y los tipos de programación: concurrente y paralela.
- Analizar los beneficios y desafíos de la programación multiproceso.

---

## ⏱️ DURACIÓN ESTIMADA

90 minutos (entre 60 y 120 minutos).

---

## 📘 ENUNCIADO

Una empresa de análisis de datos recibe constantemente grandes volúmenes de información que deben ser procesados. Actualmente, el procesamiento de cada lote de datos se realiza de forma secuencial, lo que ralentiza la entrega de resultados.

La dirección de la empresa quiere evaluar cómo la programación multihilo y multiproceso puede mejorar el rendimiento, aprovechando mejor los recursos del hardware moderno.

Se te pide desarrollar un programa en Python que simule el procesamiento de varios "lotes de datos" y comparar el rendimiento en distintos modelos de ejecución.

---

## 🧩 TAREAS A REALIZAR

### 1. Función de simulación de procesamiento

Crea una función en Python:

```python
procesar_datos(id_lote, duracion_simulada)
```

Esta función debe:

- Mostrar un mensaje indicando el inicio del procesamiento del lote.
- Simular una tarea que tarda un tiempo determinado (por ejemplo, usando `time.sleep()`).
- Mostrar un mensaje indicando el final del procesamiento.

---

## 2. Implementación monohilo (secuencial)

- Ejecuta la función anterior para 5 lotes de datos distintos de forma secuencial.
- Mide el tiempo total de ejecución.
- Muestra el resultado por pantalla.

---

## 3. Implementación multihilo (concurrente)

- Utiliza el módulo `threading` de Python.
- Ejecuta los 5 lotes de datos de forma concurrente mediante hilos.
- Asegúrate de esperar a que todos los hilos finalicen.
- Mide el tiempo total de ejecución.

---

## 4. Implementación multiproceso (paralela)

- Utiliza el módulo `multiprocessing`.
- Ejecuta los 5 lotes en procesos independientes.
- Asegúrate de esperar a que todos los procesos finalicen.
- Mide el tiempo total de ejecución.

---

## 5. Análisis de resultados

Debes analizar y explicar:

- Comparación de tiempos entre las tres implementaciones.
- Diferencias entre:
  - ejecución secuencial
  - concurrencia
  - paralelismo
- Explicación basada en los conceptos teóricos de:
  - procesos
  - hilos
  - multitarea

Además:

- Indica si se ha conseguido paralelismo real.
- Explica en función de los núcleos de la CPU.

---

## 6. Sincronización

Responde brevemente:

- ¿Qué ocurriría si los procesos/hilos compartieran recursos?
- ¿Por qué sería necesaria la sincronización?
- ¿Qué es la exclusión mutua?

---

## ⭐ SE VALORARÁ POSITIVAMENTE

- Claridad en la explicación teórica.
- Uso de comentarios en el código.
- Comprensión de cuándo usar hilos vs procesos.
- Organización del código y documentación.

---

## 📊 CRITERIOS DE EVALUACIÓN

### 🧠 Comprensión conceptual

- 0-20% → No se evidencian conceptos de proceso/hilo/multitarea.
- 20-40% → Nociones básicas sin relación clara con el problema.
- 40-60% → Identifica conceptos, pero con limitaciones.
- 60-80% → Comprende multitarea y concurrencia correctamente.
- 80-100% → Comprensión profunda y correcta aplicación de conceptos.

---

### 💻 Implementación del código

- 0-20% → Código inexistente o no funcional.
- 20-40% → Código incompleto o con errores graves.
- 40-60% → Versiones parcialmente funcionales.
- 60-80% → Funciona correctamente, con posibles mejoras.
- 80-100% → Código correcto, limpio y bien estructurado.

---

### 📈 Análisis y comparación

- 0-20% → No hay análisis o es incorrecto.
- 20-40% → Análisis superficial sin base teórica.
- 40-60% → Comparación con explicaciones limitadas.
- 60-80% → Comparación correcta con base teórica.
- 80-100% → Análisis exhaustivo y bien justificado.

---

### 🔒 Sincronización

- 0-20% → No se aborda.
- 20-40% → Se menciona sin comprensión.
- 40-60% → Reconoce necesidad sin profundizar.
- 60-80% → Explica sincronización y exclusión mutua.
- 80-100% → Explicación profunda con mecanismos (semáforos, monitores, etc.).

---

## 📦 ENTREGA

Debes generar:

- Los scripts Python necesarios para cada implementación:
  - monohilo
  - multihilo
  - multiproceso

- Un archivo `solucion.md` que incluya:
  - análisis de resultados
  - explicación teórica
  - comparación de tiempos
  - conclusiones
