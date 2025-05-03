# Ficha Específica – `gestion_nfc.py`

## Nombre del archivo:
`gestion_nfc.py`

## Responsabilidad principal:
Gestionar la evaluación de eventos de activación provenientes de la lectura de identificadores NFC, determinando si deben disparar la activación del sistema NORA.

## Entradas esperadas:
- Eventos de detección NFC (`EVT_NFC_UID_DETECTED`).
- Configuraciones dinámicas (lista de UIDs autorizados, modo de operación).

## Salidas generadas:
- Eventos de activación condicional basada en validación NFC.
- Eventos asociados:
  - `EVT_ACTIVATION_CONFIRMED`
  - `EVT_ACTIVATION_DENIED`

## Funcionalidades principales:
- Comparación del UID leído con la lista de autorizaciones.
- Validación de accesos autorizados o rechazo.
- Emisión de eventos de activación o denegación en función del resultado.
- Registro opcional de intentos fallidos o aceptados.

## Dependencias técnicas:
- `json` – Gestión de listas de UIDs autorizados.
- `datetime` – Registro de eventos.
- `eventos_activacion.py` – Emisión de eventos estandarizados.

