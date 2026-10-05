import os
import json

def crear_estructura_proyecto(num_semanas=16):
    print(" Creando arquitectura de carpetas para el proyecto...\n")
    
    # 1. Directorios principales
    dir_banco = "banco_problemas"
    dir_salida = "salida_semanas"
    
    os.makedirs(dir_banco, exist_ok=True)
    os.makedirs(dir_salida, exist_ok=True)
    print(f"  [+] Carpetas principales verificadas: '{dir_banco}/' y '{dir_salida}/'")
    
    # 2. Plantilla base para cada archivo JSON
    plantilla_json = [
        {
            "id": "SEM01_P01",
            "semana": 1,
            "enunciado": "Escribe aquí el enunciado del problema...",
            "requiere_grafica": True,
            "observaciones": ""
        }
    ]
    
    # 3. Generar carpetas y archivos por cada semana (01 a 16)
    for i in range(1, num_semanas + 1):
        num_str = f"{i:02d}"  # Formato 01, 02, ..., 16
        
        # A. Crear subcarpeta de salida para las imágenes, .tex y .pdf de la semana
        carpeta_semana_salida = os.path.join(dir_salida, f"semana_{num_str}")
        os.makedirs(carpeta_semana_salida, exist_ok=True)
        
        # B. Crear archivo JSON base en banco_problemas/ si aún no existe
        ruta_json_semana = os.path.join(dir_banco, f"semana_{num_str}.json")
        if not os.path.exists(ruta_json_semana):
            # Ajustar la plantilla con el número de semana correspondiente
            plantilla_semana = [
                {
                    "id": f"SEM{num_str}_P01",
                    "semana": i,
                    "enunciado": f"Ejemplo de problema para la Semana {i}",
                    "requiere_grafica": False,
                    "observaciones": ""
                }
            ]
            with open(ruta_json_semana, "w", encoding="utf-8") as f:
                json.dump(plantilla_semana, f, indent=2, ensure_ascii=False)
            print(f"  [+] Creada estructura y archivo: {dir_banco}/semana_{num_str}.json")
        else:
            print(f"  [=] El archivo {dir_banco}/semana_{num_str}.json ya existía (sin cambios).")

    print("\n ¡Estructura de carpetas y archivos lista exitosamente!")

if __name__ == "__main__":
    crear_estructura_proyecto(num_semanas=16)