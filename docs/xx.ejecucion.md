## xx. Ejecución del Proyecto NORA – Bitácora Técnica

Este documento sirve como registro paso a paso del proceso de ejecución técnica del proyecto NORA, en orden cronológico y estructurado. Permite trazar cómo se ha ido implementando y desplegando cada parte del sistema.

Se actualizará progresivamente con cada acción relevante, incluyendo comandos ejecutados, archivos creados, estructura establecida y decisiones técnicas documentadas.

---

### 🟢 Paso 1: Generación de estructura de carpetas lógicas (`src/`)

**Fecha:** [Especificar]

**Acción:** Creación de la estructura modular del sistema dentro de `src/` mediante script automatizado.

**Ubicación del script:** `src/utils/estructura_src.py`

**Comando ejecutado:**
```bash
cd src
python utils/estructura_src.py
```

**Resultado:**
- Carpetas creadas: `vision/`, `voz/`, `interfaz/`, `control/`, `sistema/`, `datos/`
- Cada una incluye su `__init__.py`

**Motivación técnica:** Permite comenzar con un diseño desacoplado y extensible. Cada carpeta corresponde a un módulo lógico autónomo del sistema.

**Notas adicionales:**
- El script ha sido corregido para **no crear la carpeta `src/`**, ya que se ejecuta desde dentro de ella.
- Ver `utils/estructura_src.py` para la versión actual.

**Referencias:**
- `02.arquitectura_logica.md`
- `estructura_src.py`

---

### 🔜 Próximos pasos previstos

1. Creación del archivo `main.py` como orquestador del sistema en modo simulación.
2. Inclusión del primer módulo lógico (`sistema/`) con definición de estados.
3. Desarrollo de un `EventManager` básico según `06.documento_eventos.md`

Este archivo se actualizará de forma incremental conforme se ejecuten nuevas acciones en el entorno local del proyecto.