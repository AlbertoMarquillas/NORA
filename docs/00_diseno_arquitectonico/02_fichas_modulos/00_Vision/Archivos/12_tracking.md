# Ficha Específica – `tracking.py`

## Nombre del archivo:
`tracking.py`

## Responsabilidad principal:
Mantener identificadores persistentes para los rostros detectados a lo largo de múltiples frames, permitiendo seguir a cada usuario individualmente dentro de la escena. Asigna ID únicos a los rostros y gestiona su continuidad o desaparición.

## Entradas esperadas:
- Coordenadas faciales `(x, y, w, h)` detectadas en cada frame.
- Opcionalmente, embeddings faciales o características adicionales para reforzar la identificación.
- Parámetros de configuración (tolerancia al movimiento, tiempo máximo de desaparición permitida).

## Salidas generadas:
- Lista de rostros activos con sus ID asociados.
- Actualizaciones de tracking: nuevo rostro detectado, rostro perdido, rostro reidentificado.
- Eventos opcionales:
  - `EVT_NEW_FACE_TRACKED`
  - `EVT_FACE_LOST`

## Funcionalidades principales:
- Asociación de nuevas detecciones con rostros existentes mediante cálculo de distancias espaciales.
- Creación de nuevos IDs para rostros no reconocidos previamente.
- Seguimiento temporal para manejar pérdidas momentáneas de detección.
- Eliminación de rostros del tracking tras tiempo de desaparición excedido.
- Emisión de eventos opcionales para cambios relevantes en el tracking.

## Dependencias técnicas:
- `NumPy` – Cálculo de distancias euclidianas y operaciones sobre bounding boxes.
- `collections` – Gestión eficiente de listas y estructuras temporales de tracking.

