import time


class ProcesadorDatos:
    """
    Clase encargada de simular el procesamiento de lotes de datos.

    Incluye dos tipos de procesamiento:
    - I/O-bound: basado en espera (sleep)
    - CPU-bound: basado en cálculo intensivo
    """

    @staticmethod
    def procesar_datos_io(id_lote: int, duracion_simulada: float) -> None:
        """
        Simula el procesamiento de un lote de datos mediante una espera.

        Este método representa una tarea I/O-bound (entrada/salida),
        donde el proceso pasa la mayor parte del tiempo esperando.

        Args:
            id_lote (int): Identificador del lote de datos.
            duracion_simulada (float): Tiempo en segundos que dura la simulación.
        """
        print(f"[INICIO] Procesando lote {id_lote}")

        # Simulación de espera (por ejemplo: red, disco, base de datos)
        time.sleep(duracion_simulada)

        print(f"[FIN] Lote {id_lote} procesado")

    @staticmethod
    def procesar_datos_cpu(id_lote: int, carga_trabajo: int) -> None:
        """
        Simula el procesamiento de un lote de datos mediante cálculo intensivo.

        Este método representa una tarea CPU-bound, donde el uso de CPU es alto.

        Args:
            id_lote (int): Identificador del lote de datos.
            carga_trabajo (int): Número de iteraciones que simulan la carga.
        """
        print(f"[INICIO] Procesando lote {id_lote}")

        resultado = 0

        # Bucle intensivo que consume CPU
        for i in range(carga_trabajo):
            resultado += i * i

        # el resultado no se usa, solo evita optimizaciones del compilador
        print(f"[FIN] Lote {id_lote} procesado | Resultado: {resultado}")
