# 🧪 Caso Práctico: Gestión Concurrente de Inventario con Hilos

---

## 🎯 OBJETIVOS

- Comprender y aplicar el concepto de hilo y programación multihilo.
- Aprender a crear y gestionar hilos en Python.
- Identificar problemas de concurrencia como la inconsistencia de memoria.
- Implementar mecanismos de sincronización (Lock/Semaphore).
- Entender el comportamiento del hilo principal y su impacto en la ejecución.

---

## ⏱️ DURACIÓN ESTIMADA

90 minutos.

---

## 📘 ENUNCIADO

Imagina que estás desarrollando un sistema de gestión de inventario para una tienda online. El sistema recibe múltiples pedidos simultáneamente, y cada pedido debe actualizar la cantidad disponible de un producto.

Actualmente, el sistema procesa los pedidos de forma secuencial, lo que genera demoras significativas. Se desea mejorar el rendimiento utilizando programación multihilo, garantizando al mismo tiempo la consistencia de los datos.

---

## 📦 CONTEXTO DEL PROBLEMA

- Stock inicial disponible: **1000 unidades**
- Cada pedido:
  - vende 1 unidad
  - decrementa el stock global

---

## 🧩 TAREAS A REALIZAR

### 1. Definición del estado global

- Define una variable global `stock_disponible = 1000`.

---

### 2. Función de procesamiento de pedidos

Crea una función:

```python
procesar_pedido(numero_pedido)
```

Debe:

- Mostrar un mensaje indicando que el pedido está siendo procesado.
- Simular una operación lenta (`time.sleep(0.01)`).
- Decrementar en 1 el `stock_disponible`.
- Mostrar el estado actualizado del stock.

---

## 3. Implementación concurrente sin sincronización

- Lanza 100 hilos, uno por cada pedido.
- Cada hilo debe recibir un identificador único.
- Ejecuta el programa.
- Observa el valor final de `stock_disponible`.

👉 **Explica:**

- ¿Es el resultado esperado (900)?
- ¿Por qué ocurre o no ocurre?

---

## 4. Identificación del problema

- Explica qué es la inconsistencia de memoria.
- Relaciónalo con la ejecución concurrente de los hilos.

---

## 5. Implementación con sincronización

- Usa un mecanismo de sincronización:
  - `threading.Lock` o `threading.Semaphore`
- Protege el acceso a `stock_disponible`.
- Define una sección crítica.

---

## 6. Ejecución con sincronización

- Ejecuta nuevamente el programa.
- Verifica que el resultado final sea correcto (**900**).

---

## 7. Comparación de resultados

Analiza:

- Diferencias entre ejecución:
  - sin sincronización
  - con sincronización
- Impacto en la consistencia de datos
- Orden de ejecución de los hilos

---

## 8. Reflexión sobre el hilo principal

Responde:

- ¿Qué ocurriría si el hilo principal se bloquea tras lanzar los hilos?
- ¿Cómo afectaría esto a la experiencia del usuario?

---

## ⭐ SE VALORARÁ POSITIVAMENTE

- Uso de hilos demonio (`daemon`) para tareas secundarias.
- Manejo básico de excepciones.
- Código claro y bien comentado.
- Comprensión de la ejecución no determinista de los hilos.

---

## 📊 CRITERIOS DE EVALUACIÓN

### 🧵 Creación y ejecución de hilos

- 0-20% → No se utilizan hilos o la creación es incorrecta.
- 20-40% → Se crean hilos, pero no se ejecutan correctamente.
- 40-60% → Hilos creados y ejecutados, con errores o sin cumplir requisitos.
- 60-80% → Hilos correctamente ejecutados, comprensión básica.
- 80-100% → Implementación óptima con comprensión clara de `Thread` y `start()`.

---

### ⚠️ Identificación de problemas

- 0-20% → No se identifica ningún problema de concurrencia.
- 20-40% → Se intuye el problema, pero no se explica correctamente.
- 40-60% → Identificación parcial con explicación limitada.
- 60-80% → Identificación correcta del problema.
- 80-100% → Explicación detallada y relacionada con secciones críticas.

---

### 🔒 Implementación de sincronización

- 0-20% → No se implementa sincronización.
- 20-40% → Implementación incorrecta o genera errores.
- 40-60% → Implementación parcial o ineficiente.
- 60-80% → Uso correcto de `Lock` o `Semaphore`.
- 80-100% → Solución robusta, eficiente y correcta.

---

### 📈 Análisis y conclusiones

- 0-20% → Sin análisis.
- 20-40% → Análisis superficial.
- 40-60% → Análisis básico.
- 60-80% → Análisis claro y fundamentado.
- 80-100% → Análisis profundo y crítico.

---

### 💻 Calidad del código

- 0-20% → Código ilegible o sin estructura.
- 20-40% → Código poco claro o mal comentado.
- 40-60% → Código funcional pero mejorable.
- 60-80% → Código limpio y estructurado.
- 80-100% → Código modular, claro y profesional.

---

## 📦 ENTREGA

Debes generar:

- Un archivo Python:
  - `inventario_concurrente.py`

- Un archivo `solucion.md` que incluya:
  - explicación del problema
  - análisis sin sincronización
  - análisis con sincronización
  - comparación de resultados
  - reflexión sobre el hilo principal
