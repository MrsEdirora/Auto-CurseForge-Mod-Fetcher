import requests
import csv
import time
import os
from project_ids import project_ids

# Configuración de la API de CurseForge
API_KEY = os.getenv("CURSEFORGE_API_KEY")  # Intentar cargar la clave de API desde las variables de entorno
if not API_KEY:
    API_KEY = input("Por favor, introduce tu clave de API de CurseForge: ").strip()
    if not API_KEY:
        print("Error: No se proporcionó una clave de API. El programa no puede continuar.")
        exit()

BASE_URL = "https://api.curseforge.com/v1"

# Encabezados para la autenticación
headers = {
    "Accept": "application/json",
    "x-api-key": API_KEY,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Función para clasificar el mod según palabras clave en su resumen
def clasificar_mod(summary):
    if not isinstance(summary, str):  # Validar que summary sea una cadena
        return "No clasificado"

    summary_lower = summary.lower()
    if "performance" in summary_lower or "optimiza" in summary_lower:
        return "Optimización / Rendimiento"
    elif "visual" in summary_lower or "gráfico" in summary_lower:
        return "Mejoras visuales / Estéticas"
    elif any(keyword in summary_lower for keyword in ["bioma", "estructura", "mundo"]):
        return "Contenido / Generación de mundo"
    elif "api" in summary_lower or "librería" in summary_lower:  # Corregido el uso de 'in'
        return "Librería / API"
    elif any(keyword in summary_lower for keyword in ["interfaz", "ui", "calidad de vida"]):
        return "Calidad de vida / Herramienta"
    else:
        return "No clasificado"

# Lista donde se almacenará la información extraída
datos_mods = []

# Validar si la lista de project_ids está vacía o contiene valores no válidos
if not project_ids or not all(isinstance(pid, int) for pid in project_ids):
    print("Error: La lista de project_ids está vacía o contiene valores no válidos. Por favor, agrega IDs válidos.")
    exit()

# Archivo de salida
output_file = "mods_info.csv"
if os.path.exists(output_file):
    print(f"El archivo {output_file} ya existe. Cambiando el nombre...")
    base, ext = os.path.splitext(output_file)
    output_file = f"{base}_{int(time.time())}{ext}"

# Recorremos cada projectID y realizamos la consulta en la API de CurseForge
total_ids = len(project_ids)
for idx, pid in enumerate(project_ids, start=1):
    print(f"Procesando {idx}/{total_ids} - ProjectID {pid}")
    url = f"{BASE_URL}/mods/{pid}"
    
    try:
        response = requests.get(url, headers=headers, timeout=20)  # Aumentado a 20 segundos
        if response.ok:
            data = response.json()
            mod_data = data.get("data", {})
            
            nombre = mod_data.get("name", f"Nombre no encontrado para ProjectID {pid}")
            resumen = mod_data.get("summary", f"Resumen no encontrado para ProjectID {pid}")
            
            categoria = clasificar_mod(resumen)
            
            datos_mods.append({
                "ProjectID": pid,
                "Nombre": nombre,
                "Resumen": resumen,
                "Categoría": categoria
            })
            print(f"Procesado ProjectID {pid} - {nombre}")
        else:
            print(f"Error al obtener datos para ProjectID {pid} - HTTP {response.status_code}")
            print(f"Detalles del error: {response.text}")
            datos_mods.append({
                "ProjectID": pid,
                "Nombre": "Error HTTP",
                "Resumen": "",
                "Categoría": ""
            })
    except requests.exceptions.Timeout:
        print(f"Tiempo de espera agotado para ProjectID {pid}")
        datos_mods.append({
            "ProjectID": pid,
            "Nombre": "Timeout",
            "Resumen": "",
            "Categoría": ""
        })
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud para ProjectID {pid}: {e}")
        datos_mods.append({
            "ProjectID": pid,
            "Nombre": "Error de solicitud",
            "Resumen": "",
            "Categoría": ""
        })
    except Exception as e:
        print(f"Excepción para ProjectID {pid}: {e}")
        datos_mods.append({
            "ProjectID": pid,
            "Nombre": "Excepción al obtener",
            "Resumen": "",
            "Categoría": ""
        })
        
    # Agrega una pequeña pausa para no sobrecargar el servidor
    time.sleep(2)  # Aumentado a 2 segundos para evitar problemas de límite de tasa

# Validar si hay datos antes de escribir el archivo CSV
if datos_mods:
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["ProjectID", "Nombre", "Resumen", "Categoría"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for mod in datos_mods:
            writer.writerow(mod)
    print(f"Proceso completado. Revisa el archivo {output_file}.")
else:
    print("No se obtuvieron datos. No se generó el archivo CSV.")

