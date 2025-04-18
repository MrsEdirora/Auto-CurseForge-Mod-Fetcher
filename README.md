# Auto CurseForge Mod Fetcher

Este proyecto permite automatizar la obtención de información sobre mods de Minecraft desde la API de CurseForge. Utiliza una lista de `project_ids` para consultar la API y clasifica los mods según palabras clave en sus descripciones.

## Requisitos Previos

Si no tienes Python ni las bibliotecas necesarias instaladas, puedes usar el archivo `setup.bat` para configurar todo automáticamente.

### Configuración Automática

1. Ejecuta el archivo `setup.bat` haciendo doble clic sobre él.
2. Sigue las instrucciones en pantalla. Si Python no está instalado, se descargará automáticamente.
3. Una vez completada la configuración, podrás ejecutar el programa.

### Configuración Manual

1. **Python 3.7 o superior**: Asegúrate de tener Python instalado en tu sistema.
2. **Bibliotecas necesarias**: Instala las dependencias ejecutando:
   ```bash
   pip install requests beautifulsoup4
   ```
3. **Clave de API de CurseForge**: Necesitas una clave de API válida para acceder a la API de CurseForge. Solicítala desde [CurseForge API](https://docs.curseforge.com/).

## Configuración del Programa

1. **Configurar la clave de API**:
   - El programa intentará cargar la clave de API desde la variable de entorno `CURSEFORGE_API_KEY`. Si no está configurada, te pedirá que la introduzcas manualmente al ejecutar el programa.

2. **Crear el archivo `project_ids.py`**:
   - Crea un archivo llamado `project_ids.py` en el mismo directorio que el script principal. Este archivo debe contener una lista de IDs de proyectos de CurseForge. Ejemplo:
     ```python
     project_ids = [659011, 352039, 55438, 479134]
     ```

## Uso

1. Ejecuta el script principal:
   ```bash
   python program.py
   ```
2. El programa consultará la API de CurseForge para cada `project_id` en la lista y clasificará los mods según palabras clave en sus descripciones.
3. Los resultados se guardarán en un archivo CSV dentro de la subcarpeta `output`.
4. El enlace directo a la página de CurseForge para cada mod se obtiene automáticamente desde la API.

## Manejo de Errores

El programa maneja los siguientes errores:
- **Clave de API no configurada**: Si no se encuentra la clave de API como variable de entorno y no se introduce manualmente, el programa finaliza.
- **Errores HTTP**: Muestra el código de estado y el contenido del error.
- **Timeouts**: Registra un error si una solicitud excede el tiempo de espera.
- **Lista de `project_ids` vacía o inválida**: El programa valida que la lista no esté vacía y que todos los elementos sean números enteros.
- **Enlace no disponible en la API**: Si la API no proporciona un enlace directo, se genera un enlace predeterminado basado en el `projectID`.

## Créditos

- **Mrs_Edirora**: Idea y dirección del proyecto.
- **GitHub Copilot**: Asistencia en el desarrollo y optimización del código.

## Licencia

Este proyecto está bajo la licencia MIT.