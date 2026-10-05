import json
import glob
import sys

def validar_archivos():
    archivos = sorted(glob.glob("banco_problemas/semana_*.json"))
    if not archivos:
        print(" No se encontraron archivos JSON en 'banco_problemas/'")
        sys.exit(1)

    errores = 0
    total_problemas = 0

    print("🔍 Validando archivos JSON de las semanas...\n")

    for ruta in archivos:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                cant = len(datos)
                total_problemas += cant
                print(f"   {ruta}: Válido ({cant} problemas detectados)")
        except json.JSONDecodeError as e:
            errores += 1
            print(f"   ERROR en {ruta}: Sintaxis inválida en la línea {e.lineno}, columna {e.colno}")

    print("\n" + "="*40)
    if errores == 0:
        print(f" Todos los JSON son válidos. Total de problemas cargados: {total_problemas}")
    else:
        print(f" Se encontraron {errores} archivo(s) con errores de formato. Corrígelos antes de continuar.")

if __name__ == "__main__":
    validar_archivos()