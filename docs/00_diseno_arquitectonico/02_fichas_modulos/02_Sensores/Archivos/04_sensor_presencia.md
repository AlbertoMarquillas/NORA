# Ficha Específica – `sensor_presencia.py`

## Nombre del archivo:
`sensor_presencia.py`

## Responsabilidad principal:
Gestionar la lectura de sensores de ultrasonidos (como HC-SR04) para detectar la presencia física de objetos o personas cercanas al sistema NORA.

## Entradas esperadas:
- Señales digitales de medición de distancia.
- Configuraciones dinámicas (distancia umbral de detección, frecuencia de lectura).

## Salidas generadas:
- Valores de distancia en centímetros o metros.
- Eventos asociados:
  - `EVT_PRESENCE_CONFIRMED`
  - `EVT_PRESENCE_LOST`

## Funcionalidades principales:
- Captura del tiempo de ida y vuelta de la señal ultrasónica.
- Conversión del tiempo medido a distancia física.
- Detección de presencia o ausencia basada en distancias configuradas.
- Emisión de eventos de detección o pérdida de presencia.
- Filtrado de lecturas erróneas o inestables.

## Dependencias técnicas:
- `gpiozero`, `RPi.GPIO` – Gestión de pines de trigger y echo.
- `time` – Medición precisa de microsegundos.
- `datetime`, `json` – Formato de eventos para emisión o registro.

