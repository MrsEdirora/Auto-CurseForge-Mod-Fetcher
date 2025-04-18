# Registro de Errores y Soluciones

Este archivo documenta los errores encontrados durante el desarrollo del proyecto y las soluciones implementadas.

---

## Error HTTP 403

### Descripción
El servidor de CurseForge devuelve un error HTTP 403 (Prohibido) al intentar realizar solicitudes a la API.

### Causa
1. La clave de API proporcionada no era válida o no tenía los permisos necesarios.
2. El servidor detectó que las solicitudes no provenían de un cliente autorizado (falta de un encabezado `User-Agent`).

### Soluciones Implementadas
1. **Validación de la clave de API**:
   - Se agregó una validación para verificar si la clave de API está configurada como variable de entorno.
   - Si no está configurada, el programa solicita al usuario que introduzca la clave manualmente.
2. **Agregar un encabezado `User-Agent`**:
   - Se agregó el siguiente encabezado a las solicitudes:
     ```
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
     ```

---

## Error: Clave de API no configurada

### Descripción
El programa no puede continuar si la clave de API no está configurada como variable de entorno y no se proporciona manualmente.

### Soluciones Implementadas
1. **Solicitud manual de la clave de API**:
   - Si la clave de API no está configurada como variable de entorno, el programa solicita al usuario que la introduzca manualmente.
2. **Mensajes de error claros**:
   - Se agregó un mensaje de error que explica cómo configurar la clave de API como variable de entorno.

---

## Error: Lista de `project_ids` vacía o inválida

### Descripción
El programa no puede continuar si la lista de `project_ids` está vacía o contiene valores no válidos.

### Soluciones Implementadas
1. **Validación de la lista**:
   - Se agregó una validación para verificar que la lista no esté vacía y que todos los elementos sean números enteros.
2. **Mensajes de error claros**:
   - Se agregó un mensaje de error que explica cómo corregir el archivo `project_ids.py`.

---

## Error: Sintaxis incorrecta en operadores lógicos

### Descripción
El programa contenía errores de sintaxis debido al uso incorrecto del operador lógico `o` en lugar de `or`.

### Soluciones Implementadas
1. **Corrección de operadores lógicos**:
   - Se corrigieron todas las instancias de `o` por `or` en el código.

---

## Error: Archivo de salida ya existente

### Descripción
Si el archivo de salida `mods_info.csv` ya existía, el programa lo sobrescribía sin generar un nuevo archivo.

### Soluciones Implementadas
1. **Generación de nombres únicos**:
   - Se agregó una verificación para cambiar el nombre del archivo de salida si ya existe, añadiendo una marca de tiempo al nombre.

---

Este archivo se actualizará con nuevos errores y soluciones a medida que se encuentren durante el desarrollo.
