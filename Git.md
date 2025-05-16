# Clasificación Temática de los Comandos de Git

Este documento recoge los temas principales abordados por los comandos de Git, organizados por ámbitos funcionales para facilitar su estudio, documentación y uso sistemático en entornos de desarrollo y control de versiones.

---

## 1. Inicialización del Repositorio

Comandos que permiten crear o clonar un repositorio Git.

* `git init [--bare] [--initial-branch <nombre>] [<directorio>]`

  * Inicializa un nuevo repositorio local vacío. La opción `--bare` crea un repositorio sin área de trabajo (solo para servidores). `--initial-branch` permite definir el nombre de la rama principal.

* `git clone <repositorio> [<directorio>] [--branch <rama>] [--depth <profundidad>] [--single-branch] [--recurse-submodules]`

  * Clona un repositorio remoto. Puede especificarse el nombre del directorio destino, la rama deseada, profundidad para clonado superficial, o incluir submódulos.

---

## 2. Configuración del Entorno

Gestiones relacionadas con la configuración de usuario, editor, alias, reglas y entorno de trabajo.

* `git config [--global | --local | --system] <clave> <valor>`

  * Establece una configuración en el ámbito especificado (global, local o del sistema). Ejemplos típicos: `user.name`, `user.email`, `core.editor`, `merge.tool`.

* `git config --get <clave>`

  * Recupera el valor actual asignado a una clave de configuración.

* `git config --unset <clave>`

  * Elimina una clave de configuración definida.

* `git config --list [--global | --local | --system]`

  * Lista todas las configuraciones activas, en el nivel especificado si se indica.

* `git config --edit [--global | --local]`

  * Abre el archivo de configuración en el editor por defecto para editarlo manualmente.

---

## 3. Estado y Exploración del Repositorio

Consulta del estado de trabajo, diferencias entre versiones y exploración del historial.

* `git status [--short] [--branch]`

  * Muestra el estado del directorio de trabajo y del área de staging. Con `--short` se obtiene un formato compacto; `--branch` muestra información de rama.

* `git diff [<rama> | <archivo>] [--staged] [--name-only] [--stat]`

  * Muestra las diferencias entre versiones, ramas o archivos. `--staged` compara con el área de staging. `--name-only` lista solo los archivos cambiados.

* `git log [<rango>] [--oneline] [--graph] [--decorate] [--stat]`

  * Muestra el historial de commits. `--oneline` condensa la salida. `--graph` dibuja una representación visual de ramas y merges.

* `git show <objeto>`

  * Muestra el contenido de un objeto Git (por ejemplo, un commit o una etiqueta).

* `git blame <archivo> [-L <inicio>,<fin>] [--show-name]`

  * Muestra línea por línea qué commit fue responsable del último cambio. `-L` restringe el rango de líneas a mostrar.

---

## 4. Gestión de Archivos y Cambios Locales

Control de archivos, su seguimiento, eliminación y restauración en el área de staging.

* `git add <archivo|directorio> [opciones]`

  * Añade archivos al área de staging. Opciones comunes: `-A` (todos), `-u` (solo los ya versionados), `-p` (por fragmentos interactivos).

* `git rm <archivo> [--cached] [-f]`

  * Elimina archivos del repositorio y del área de trabajo. `--cached` los elimina solo del área de staging. `-f` fuerza la eliminación si están modificados.

* `git mv <origen> <destino>`

  * Renombra o mueve archivos controlados por Git. Equivale a mover + eliminar + añadir.

* `git restore [<archivo>] [--source <commit>] [--staged] [--worktree]`

  * Restaura archivos desde el historial o desde el staging. `--staged` afecta al área de staging; `--worktree` al área de trabajo.

---

## 5. Commits

Registro de cambios en el historial del repositorio.

* `git commit [-m <mensaje>] [--amend] [--no-edit] [--allow-empty] [--signoff]`

  * Crea un nuevo commit con los cambios del área de staging. `-m` permite definir un mensaje inline. `--amend` modifica el último commit. `--allow-empty` fuerza un commit sin cambios. `--signoff` añade una firma de autor.

* `git commit --amend [--no-edit] [--reset-author]`

  * Reemplaza el último commit con uno nuevo. Puede conservar el mensaje anterior (`--no-edit`) o cambiar el autor (`--reset-author`).

---

## 6. Branching y Fusión (Ramas)

Creación, gestión, cambio y combinación de ramas.

* `git branch [<nombre>] [-d | -D] [-m <nuevo_nombre>] [-r] [-a]`

  * Lista, crea o elimina ramas. `-d` elimina una rama; `-D` fuerza la eliminación. `-m` renombra. `-r` muestra ramas remotas. `-a` muestra todas.

* `git checkout <rama>` / `git checkout -b <nueva_rama>`

  * Cambia de rama. Con `-b`, crea una nueva rama y se posiciona en ella. Esta sintaxis es compatible pero ha sido sustituida por `git switch`.

* `git switch <rama>` / `git switch -c <nueva_rama>`

  * Cambia de rama (alternativa moderna a `checkout`). `-c` crea y cambia a una nueva rama.

* `git merge <rama>` \[--no-ff] \[--squash] \[--commit]

  * Fusiona la rama especificada con la actual. `--no-ff` evita "fast-forward". `--squash` aúna los cambios sin commit. `--commit` obliga a crear commit.

* `git rebase [<rama>] [--interactive | -i] [--onto <base>]`

  * Reaplica commits sobre otra base. `--interactive` permite editar, reordenar o eliminar commits intermedios. `--onto` especifica una base distinta.

---

## 7. Sincronización con Repositorios Remotos

Enlace con servidores remotos para compartir código y sincronizar ramas.

* `git remote [-v] [add <nombre> <url>] [remove <nombre>] [rename <antiguo> <nuevo>]`

  * Gestiona los remotos del repositorio. `-v` muestra las URLs. `add` añade un nuevo remoto. `remove` lo elimina. `rename` cambia su nombre.

* `git fetch [<remoto>] [<rama>] [--all] [--prune]`

  * Descarga objetos y referencias desde un remoto. `--all` afecta a todos los remotos. `--prune` elimina referencias remotas obsoletas.

* `git pull [<remoto>] [<rama>] [--rebase] [--no-commit]`

  * Descarga y fusiona cambios de un remoto. `--rebase` reaplica los commits locales encima. `--no-commit` evita crear un commit automático.

* `git push [<remoto>] [<rama>] [--force] [--tags] [--set-upstream]`

  * Sube cambios al repositorio remoto. `--force` sobrescribe. `--tags` sube etiquetas. `--set-upstream` enlaza rama local con remota.

---

## 8. Resolución de Conflictos

Herramientas para manejar conflictos surgidos durante fusiones o rebase.

* `git mergetool [--tool=<nombre>] [--no-prompt]`

  * Abre una herramienta de resolución de conflictos visual configurada. `--tool` especifica la herramienta. `--no-prompt` evita confirmaciones interactivas.

* `git diff [--base] [--ours] [--theirs] [<archivo>]`

  * Muestra diferencias entre versiones en conflicto. `--base`, `--ours`, `--theirs` permiten comparar las distintas ramas implicadas.

* `git status`

  * Muestra el estado del repositorio, incluyendo archivos en conflicto.

* `git restore --staged <archivo>` / `git checkout --ours|--theirs <archivo>`

  * Recupera versiones específicas en conflicto para resolver manualmente.

* `git add <archivo>`

  * Marca un conflicto como resuelto una vez editado el archivo.

---

## 9. Reescritura y Limpieza del Historial

Modificación, reversión o limpieza de commits previos.

* `git reset [--soft | --mixed | --hard] [<commit>]`

  * Reposiciona la rama actual al commit indicado. `--soft` conserva staging y trabajo, `--mixed` lo borra del staging, `--hard` lo borra completamente.

* `git revert <commit> [--no-commit] [--edit]`

  * Crea un nuevo commit que revierte los cambios de uno anterior. `--no-commit` prepara el cambio sin commitear. `--edit` abre el editor.

* `git rebase [<base>] [--interactive | -i] [--autosquash]`

  * Reaplica una serie de commits sobre otra base. `--interactive` permite editar cada paso. `--autosquash` reorganiza commits marcados como fixup/squash.

* `git cherry-pick <commit> [--no-commit] [--edit]`

  * Aplica un commit específico sobre la rama actual. `--no-commit` aplica sin generar commit. `--edit` abre el mensaje para modificarlo.

* `git reflog [<rama>]`

  * Muestra el historial de movimientos de las referencias (incluye commits descartados o rebases pasados).

---

## 10. Inspección y Comparación

Comandos para comparar ramas, archivos y commits.

* `git diff [<rama1> <rama2>] [<archivo>] [--name-only] [--stat]`

  * Compara contenidos entre ramas, commits o archivos. `--name-only` muestra solo nombres de archivos. `--stat` da un resumen estadístico.

* `git log [<rango>] [--oneline] [--graph] [--decorate] [--stat] [--patch]`

  * Muestra el historial de commits. `--patch` añade diferencias línea por línea. `--graph` dibuja una estructura en árbol.

* `git show <objeto>`

  * Muestra el contenido y metadatos de un objeto Git (commit, tag, etc). Equivalente a una combinación de `log` y `diff`.

* `gitk [<rango>]`

  * Interfaz gráfica para visualizar el historial de commits, ramas y fusiones.

---

## 11. Etiquetado

Creación y manejo de etiquetas para marcar versiones o lanzamientos.

* `git tag [<nombre>] [<commit>]`

  * Lista todas las etiquetas o crea una nueva etiqueta ligera sobre el commit actual o indicado.

* `git tag -a <nombre> -m <mensaje> [<commit>]`

  * Crea una etiqueta anotada con mensaje y metadatos. Puede apuntar a un commit específico.

* `git tag -d <nombre>`

  * Elimina una etiqueta local.

* `git push origin <nombre>`

  * Sube una etiqueta individual al repositorio remoto.

* `git push origin --tags`

  * Sube todas las etiquetas locales al repositorio remoto.

* `git show <etiqueta>`

  * Muestra la información asociada a una etiqueta (anotada) y el commit al que apunta.

---

## 12. Stash (Almacenamiento Temporal)

Guardar cambios no committeados para recuperarlos más tarde.

* `git stash [push] [-m <mensaje>] [--keep-index] [--include-untracked]`

  * Guarda los cambios actuales del directorio de trabajo. `--keep-index` mantiene cambios staged. `--include-untracked` incluye archivos no versionados.

* `git stash list [--name-status]`

  * Muestra la lista de elementos guardados en el stash. `--name-status` incluye detalles sobre los archivos.

* `git stash show [<stash>] [--patch]`

  * Muestra los cambios de un stash específico. `--patch` muestra las diferencias detalladas.

* `git stash apply [<stash>] [--index]`

  * Aplica un stash sin eliminarlo. `--index` intenta restaurar también el área de staging.

* `git stash pop [<stash>]`

  * Aplica un stash y lo elimina de la lista.

* `git stash drop <stash>`

  * Elimina un stash específico sin aplicarlo.

* `git stash clear`

  * Elimina todos los elementos del stash.

---

## 13. Submódulos

Incorporación y actualización de repositorios como dependencias.

* `git submodule add <url> [<ruta>]`

  * Añade un repositorio como submódulo en la ruta especificada. La URL puede ser local o remota.

* `git submodule init`

  * Inicializa las entradas de submódulo en `.git/config`, según el contenido del archivo `.gitmodules`.

* `git submodule update [--init] [--remote] [--merge | --rebase]`

  * Actualiza el contenido de los submódulos. `--init` inicializa si no está hecho. `--remote` extrae la última versión del repositorio remoto.

* `git submodule status`

  * Muestra el estado de los submódulos (commit actual y posibles cambios locales).

* `git submodule deinit <ruta>`

  * Desactiva un submódulo y limpia la entrada en `.git/config`.

* `git submodule foreach <comando>`

  * Ejecuta un comando en cada submódulo recursivamente.

---

## 14. Hooks (Automatización de Tareas)

Scripts que se ejecutan en eventos definidos del ciclo de vida de Git.

* Ubicación: `.git/hooks/`

  * Carpeta local del repositorio donde se almacenan los hooks.

* Hooks comunes disponibles:

  * `pre-commit`: Se ejecuta antes de que se confirme un commit. Útil para validaciones.
  * `commit-msg`: Se ejecuta después de redactar el mensaje de commit, permite validarlo o modificarlo.
  * `post-commit`: Se lanza justo después de hacer un commit.
  * `pre-push`: Se ejecuta antes de hacer un push.
  * `pre-rebase`, `pre-merge`, `post-merge`, etc.: Se ejecutan en sus respectivos momentos del flujo.

* Características:

  * Se trata de scripts ejecutables (normalmente bash, Python, etc.).
  * No están activados por defecto; los archivos vienen con extensión `.sample`.
  * No se sincronizan con el repositorio remoto (no se versionan por defecto).

---

## 15. Análisis y Depuración Avanzada

Utilidades para rastrear errores, validar integridad o mejorar rendimiento.

* `git bisect start`

  * Inicia una búsqueda binaria entre un commit correcto y uno con errores.

* `git bisect bad [<commit>]`

  * Marca el commit actual o indicado como erróneo.

* `git bisect good [<commit>]`

  * Marca el commit actual o indicado como correcto.

* `git bisect reset`

  * Finaliza la búsqueda binaria y vuelve al estado inicial.

* `git blame <archivo> [-L <inicio>,<fin>] [--reverse] [--porcelain]`

  * Atribuye cada línea del archivo al último commit que la modificó. `--reverse` invierte el seguimiento, `--porcelain` da formato scriptable.

* `git fsck [--full] [--lost-found] [--name-objects]`

  * Verifica la integridad de los objetos del repositorio. `--lost-found` muestra objetos huérfanos.

* `git gc [--aggressive] [--prune=<fecha>]`

  * Realiza una recolección de basura para optimizar espacio. `--aggressive` maximiza la compresión. `--prune` elimina objetos inalcanzables antiguos.

---

## 16. Trabajo Colaborativo / Parches

Creación, envío y aplicación de parches entre desarrolladores.

* `git format-patch [<rango>] [--stdout] [--cover-letter]`

  * Genera archivos de parche desde commits recientes. `--stdout` imprime en salida estándar. `--cover-letter` genera plantilla de correo.

* `git apply [<archivo.patch>] [--check] [--reverse] [--index]`

  * Aplica un parche sin requerir historial de commits. `--check` valida sin aplicar. `--reverse` revierte el parche. `--index` verifica coincidencias.

* `git am [<archivo.patch>] [--signoff] [--interactive] [--3way]`

  * Aplica parches formateados como correo (desde `format-patch`). `--signoff` añade firma, `--3way` intenta fusión por 3 vías si falla.

* `git send-email <parches> [--to=<email>] [--cc=<email>] [--subject=<asunto>] [--annotate]`

  * Envía parches por correo electrónico. `--annotate` permite editar antes de enviar. Requiere configuración SMTP previa.

---
