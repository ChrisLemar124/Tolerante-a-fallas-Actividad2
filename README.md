# Proyecto: Tolerancia a fallas (Actividad 2)

Descripción
- Este repositorio contiene dos scripts de ejemplo que calculan la multiplicación de matrices, guardan el resultado en disco usando `pickle`, y luego lo cargan para ser leído por otro script. El objetivo es demostrar persistencia de resultados para tolerancia a fallas (checkpointing / recuperación).

Archivos
- [Act2T.py](Act2T.py): Define dos matrices, las multiplica con `numpy`, guarda el resultado en `pesos.pkl` usando `pickle.dump` y lo imprime.
- [Act2R.py](Act2R.py): Abre `pesos.pkl`, carga el objeto con `pickle.load` y muestra la forma y contenido de la matriz resultante.

Detalle del código

Act2T.py
- Definición de matrices `matriz_A` y `matriz_B`: listas de listas (20x20).
- `multiplicar_matrices(matriz_A, matriz_B)`: valida dimensiones y rectangularidad, convierte a `numpy.array` y utiliza `np.dot` para multiplicar.
- `guardar_matriz_resultasdo(matriz, nombre_archivo)`: abre un archivo en modo binario y serializa la matriz con `pickle.dump`.
- Flujo: calcula `valor = multiplicar_matrices(...)`, guarda en `pesos.pkl` y luego imprime el resultado.

Act2R.py
- Simple lector: abre `pesos.pkl` en modo binario lectura, carga el objeto con `pickle.load`, y imprime `pesos.shape` y `pesos`.

Uso de `pickle` para tolerancia a fallas
- Persistencia / checkpointing: guardar el resultado intermedio (aquí la matriz producto) permite recuperar el estado tras un fallo o reinicio sin reejecutar todo el cálculo.
- Latencia vs tolerancia a fallas: almacenar checkpoints reduce la ventana de trabajo perdido (menor latencia en recuperación) y permite reanudar o repartir trabajo entre procesos.
- Consideraciones de seguridad: `pickle` puede ejecutar código arbitrario al deserializar. NUNCA cargue archivos pickle procedentes de fuentes no confiables.
- Recomendaciones para tolerancia robusta:
  - Añadir control de errores al guardar/cargar (try/except, validación de existencia de archivo).
  - Verificar integridad (hash/firmas) del archivo antes de cargar.
  - Para datos numéricos puros, considerar `numpy.save` / `numpy.savez` o formatos seguros como HDF5 (`h5py`) o `np.savez_compressed`.
  - Si necesita serialización con seguridad y compatibilidad, evaluar `json` (con conversión) o `joblib` para objetos numpy grandes.

Cómo ejecutar
- Requisitos: Python 3.x y `numpy` instalado.

Ejecutar producción del archivo `pesos.pkl`:
```
python Act2T.py
```

Luego leer el archivo generado:
```
python Act2R.py
```

Mejoras sugeridas
- Añadir manejo de excepciones en ambos scripts.
- Generar y comprobar un hash (SHA256) del archivo `pesos.pkl` al guardarlo y verificarlo al cargar.
- En escenarios distribuidos, usar almacenamiento compartido o base de datos para checkpointing y llevar control de versiones de checkpoints.

Archivo creado: [README.md](README.md)
