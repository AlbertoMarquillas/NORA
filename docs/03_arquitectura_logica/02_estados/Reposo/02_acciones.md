# Acciones realizadas – Estado: Reposo

Durante el estado **Reposo**, NORA minimiza su actividad funcional, reduciendo el consumo de energía y desactivando los módulos no esenciales. El sistema entra en una fase pasiva, donde únicamente se mantienen activos los sensores de activación y los servicios básicos de vigilancia para reanudar el funcionamiento en caso necesario.

---

## 1. Desactivación o suspensión de módulos

- Apagado o paso a modo de espera de los módulos `voz/`, `vision/`, `interfaz/` y `control/`
- Detención del seguimiento facial, reconocimiento de voz y motores de expresión
- Liberación de recursos computacionales no críticos

---

## 2. Activación de vigilancia mínima

- Módulo `activacion/` permanece activo con sensores seleccionados:
  - Sensor NFC (para evento `EVT_NFC_ACTIVATE`)
  - Sensor de proximidad o ultrasonido (si habilitado)
  - Detección de hotword en bajo nivel (si configurado)

---

## 3. Señalización visual y física

- Pantalla OLED/TFT apagada o en modo "reposo visual" (oscura o símbolo estático)
- LEDs RGB apagados o en estado neutro (por ejemplo, blanco tenue o azul fijo)
- Servos en posición base o completamente desactivados

---

## 4. Monitorización del entorno

- Registro periódico del estado de los sensores ambientales si se permite (`ENV_MONITOR_PASSIVE = True`)
- Supervisión de temperatura interna del sistema y nivel de carga si aplica

---

## 5. Evaluación de reactivación

- Espera activa de eventos de activación para transición a `Activado`
- Los agentes pueden mantener umbrales de activación modificados por contexto (por ejemplo, periodo nocturno → activación más exigente)

---

## Indicadores activos del sistema

| Componente        | Estado durante Reposo                      |
|-------------------|---------------------------------------------|
| voz/              | Desactivado o en escucha mínima (opcional) |
| vision/           | Apagado o con vigilancia de movimiento (si habilitado) |
| sensores/         | NFC y proximidad activos                   |
| pantalla facial   | Apagada o símbolo de reposo                |
| LEDs RGB          | Neutros o apagados                         |
| servomotores      | Posición base o desenergizados             |
