# Ficha Específica – `reconocimiento_usuario.py`

## Nombre del archivo:
`reconocimiento_usuario.py`

## Responsabilidad principal:
Asociar los rostros detectados en la escena con perfiles de usuario previamente registrados, permitiendo a NORA personalizar la interacción en función de la identidad reconocida.

## Entradas esperadas:
- Imagen facial recortada o embeddings faciales del rostro detectado.
- Base de datos local de perfiles de usuario registrados (embeddings y metadatos asociados).
- Parámetros de configuración (umbral de similitud, número máximo de intentos de identificación).

## Salidas generadas:
- Identidad de usuario reconocida o indicación de rostro desconocido.
- Nivel de confianza en la identificación.
- Eventos asociados:
  - `EVT_USER_RECOGNIZED`
  - `EVT_UNKNOWN_USER`

## Funcionalidades principales:
- Extracción de características faciales si no están precalculadas.
- Comparación entre embeddings del rostro detectado y la base de usuarios.
- Determinación de correspondencia positiva o negativa basada en umbrales de similitud.
- Actualización opcional de embeddings dinámicamente para mejorar la precisión.
- Emisión de eventos internos notificando reconocimiento o anonimato.

## Dependencias técnicas:
- `TensorFlow`, `PyTorch` o librerías equivalentes para manejo de embeddings faciales.
- `NumPy` – Cálculo de distancias métricas entre vectores de características.
- `OpenCV` – Procesamiento de imágenes si se requiere recorte o normalización adicional.
- `utils_datos.py` – Acceso y gestión de la base de datos de usuarios registrados.

