# Descripción – Interacción Verbal

La interacción verbal es uno de los pilares principales del sistema NORA. Permite al usuario emitir comandos o consultas mediante la voz, recibiendo respuestas habladas y expresivas por parte del asistente. Este tipo de interacción se basa en tecnologías de reconocimiento automático de voz (ASR), interpretación de intención (NLP ligero), y síntesis de voz (TTS).

---

## 1. Objetivo

Permitir una comunicación natural y multimodal entre el usuario y NORA, facilitando acciones cotidianas sin necesidad de contacto físico ni interfaces gráficas. Las respuestas no solo incluyen voz, sino también expresiones faciales, iluminación o acciones en el sistema.

---

## 2. Componentes principales

* **voz/asr.py**: módulo de entrada por voz, encargado del reconocimiento automático de voz.
* **dialogo/interpretador.py**: procesamiento de intención y validación de comandos.
* **voz/tts.py**: generación de la respuesta hablada por NORA.
* **agentes/validador\_contexto.py**: filtra o transforma la intención según el estado del sistema.

---

## 3. Flujo general de una interacción verbal

```plaintext
[Usuario habla] → [ASR reconoce texto] → [Interpretador analiza intención]
              → [Agente valida acción] → [Sistema ejecuta] → [TTS responde]
```

---

## 4. Características operativas

* La entrada por voz está habilitada en `STATE_ACTIVE_WAIT` o superior.
* La activación previa puede provenir de hotword, presencia, rostro o botón.
* Los comandos verbales pueden replicar funcionalidades de la GUI escrita.
* Se soporta diálogo secuencial básico (multi-turn).

---

## 5. Categorías de comandos soportados (resumen)

* Consultas: hora, fecha, agenda
* Comandos: encender/apagar, mostrar, iniciar
* Gestión personal: notas, hábitos, recordatorios
* Diálogo social básico: saludo, despedida, ánimo

Cada comando tiene un patrón de entrada esperable y uno o varios patrones de respuesta parametrizados.

---

La interacción verbal permite que NORA funcione como un asistente autónomo, expresivo y reactivo, sin necesidad de dispositivos de entrada tradicionales. Su correcto funcionamiento depende tanto de la fiabilidad del ASR como de la claridad en los flujos conversacionales definidos.
