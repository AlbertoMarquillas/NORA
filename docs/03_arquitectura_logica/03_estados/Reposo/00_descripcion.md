# Descripción funcional – Estado: Reposo

El estado **Reposo** representa la condición de mínima actividad del sistema NORA. En esta fase, todos los módulos no esenciales se encuentran apagados o en modo de bajo consumo, y el sistema suspende temporalmente la mayoría de sus funciones sensoriales, cognitivas y expresivas.

Este estado tiene como objetivo:

- Reducir el consumo energético.
- Aumentar la vida útil de los periféricos.
- Minimizar la intrusión en el entorno cuando no hay intención de interacción.

Durante **Reposo**, el sistema permanece latente pero con mecanismos de activación activos, tales como sensores de proximidad, entradas NFC o vigilancia visual mínima (si se ha configurado como disponible en segundo plano).

Este estado se considera el punto de partida y final del ciclo de interacción. Toda activación del sistema se origina desde `Reposo`, y en ausencia de interacción sostenida o ante condiciones de inactividad prolongada, el sistema retorna a este estado.

**Importancia del estado:**

El estado **Reposo** es clave para garantizar un comportamiento no intrusivo, optimizado energéticamente y respetuoso con el contexto ambiental. También permite implementar lógica de "despertar" basada en intención real del usuario.
