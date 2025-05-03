## 15. Módulo de Almacenamiento

### 15.1. Descripción General

El módulo de almacenamiento de NORA está compuesto por dos unidades de disco conectadas por USB a la Raspberry Pi 4:

* Un **SSD** de alta velocidad para operaciones críticas y procesamiento rápido.
* Un **HDD** de alta capacidad para almacenamiento masivo y datos persistentes.

Esta separación permite optimizar el rendimiento del sistema, asignando tareas según la velocidad y naturaleza del acceso a datos.

---

### 15.2. Arquitectura Física

Cada unidad de almacenamiento se conecta mediante un adaptador SATA–USB 3.0. Ambos adaptadores están conectados a un **hub USB 3.0 con alimentación externa**, para garantizar un suministro eléctrico estable sin sobrecargar los puertos de la Raspberry Pi.

#### Componentes:

* 1 × SSD 2.5" (ej. 128 GB, formato SATA)
* 1 × HDD 2.5" (ej. 1 TB o más, formato SATA)
* 2 × adaptadores SATA–USB 3.0 compatibles con Raspberry Pi
* 1 × Hub USB 3.0 alimentado externamente

---

### 15.3. Montaje Lógico del Sistema

#### SSD → `/mnt/ssd`

* Sistema de ficheros: `ext4`
* Usos:

  * Carpeta `models/` para redes neuronales
  * Caché de inferencia, archivos temporales
  * Swap o rootfs (si se arranca desde SSD)

#### HDD → `/mnt/hdd`

* Sistema de ficheros: `ext4`
* Usos:

  * Carpeta `datos/` para logs, grabaciones, registros de sensores
  * Almacenamiento de largo plazo
  * Backups y datasets de entrenamiento

---

### 15.4. Configuración en el Sistema Operativo

Se recomienda montar ambos discos automáticamente en el arranque mediante `/etc/fstab`. Para ello, se identifican los UUID con `blkid` y se añaden entradas como:

```fstab
UUID=<UUID_SSD> /mnt/ssd ext4 defaults 0 2
UUID=<UUID_HDD> /mnt/hdd ext4 defaults 0 2
```

---

### 15.5. Consideraciones Técnicas

* Ambos discos deben tener una **alimentación estable**, por lo que se descarta alimentarlos directamente desde los puertos USB de la RPi.
* Se recomienda uso de `ext4` si no se requiere compatibilidad con otros sistemas operativos.
* Ventilar adecuadamente el recinto si los discos están montados en el interior del chasis.

---

### 15.6. Conclusión

El sistema dual de almacenamiento mejora la robustez y eficiencia operativa de NORA. El SSD proporciona velocidad en tareas críticas de procesamiento, mientras que el HDD asegura persistencia y volumen para datos históricos. Esta arquitectura es flexible, escalable y apropiada para un sistema embebido avanzado como NORA.
