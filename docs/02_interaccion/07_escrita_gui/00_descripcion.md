# Descripción – Interacción Escrita por Interfaz Gráfica

Este documento define la interacción basada en texto entre el usuario y NORA mediante una interfaz gráfica. Esta vía permite emitir comandos, preguntas o introducir contenido escrito en lugar de usar la voz, replicando la mayoría de funcionalidades disponibles en la interacción verbal.

---

## 1. Objetivo

Permitir que el usuario interactúe con NORA de manera precisa, silenciosa y accesible a través de una interfaz visual, ya sea en entorno local o remoto, sin requerir entrada por voz.

---

## 2. Casos de uso típicos

* Introducir notas o recordatorios manualmente
* Consultar la agenda mediante texto escrito
* Ejecutar comandos como “Enciende la luz” desde una terminal GUI
* Interactuar con expresividad mediante botones o formularios escritos

---

## 3. Características funcionales

* Interfaz gráfica con campo de entrada de texto y zona de respuesta
* Soporte para formularios y comandos en lenguaje natural
* Equivalencia total con las funciones accesibles por voz
* Retroalimentación textual y visual inmediata

---

## 4. Módulos implicados

* `interfaz_escrita/entrada.py`: recepción de texto desde GUI
* `dialogo/interpretador.py`: análisis de intención
* `datos/` o `accionadores/`: ejecución del comando correspondiente
* `interfaz_escrita/respuesta.py`: generación de la respuesta visual

---

## 5. Ventajas

* Acceso en entornos donde la voz no es viable (ruido, privacidad)
* Mayor control del contenido introducido
* Permite trabajar con logs, correcciones o ajustes sin errores de reconocimiento

---

Esta modalidad amplía la accesibilidad de NORA, reforzando su flexibilidad y adaptabilidad a distintos contextos de uso sin perder coherencia funcional con el resto de subsistemas.
