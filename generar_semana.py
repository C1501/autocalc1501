import argparse
import json
import os
import re
import sys
import subprocess
import time
from google import genai
from google.genai import types

# Inicializar cliente de Google GenAI
client = genai.Client()

MODELOS_PREFERIDOS = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash"
]

def obtener_argumentos():
    parser = argparse.ArgumentParser(description="Generador de Fichas para IEEE Two-Column.")
    parser.add_argument("semana", type=int, help="Número de semana a procesar (ej. 1, 2, 3)")
    return parser.parse_args()

def cargar_problemas(json_path):
    if not os.path.exists(json_path):
        print(f"Error: No se encontró el archivo {json_path}")
        sys.exit(1)
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def crear_estructura_directorios(semana_str):
    dirs = [
        f"semana_{semana_str}",
        os.path.join(f"semana_{semana_str}", "graficas"),
        os.path.join(f"semana_{semana_str}", "tex_soluciones")
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def extraer_bloque_codigo(texto, lenguaje):
    """Extrae el contenido dentro de bloques ```lenguaje ... ```."""
    patron = rf"```{lenguaje}\s*(.*?)\s*```"
    coincidencias = re.findall(patron, texto, re.DOTALL | re.IGNORECASE)
    if coincidencias:
        return "\n\n".join(coincidencias).strip()
    return None

def limpiar_fragmento_tex(texto_raw):
    """Limpia marcas Markdown y etiquetas de documento en el código LaTeX."""
    tex = extraer_bloque_codigo(texto_raw, "latex") or extraer_bloque_codigo(texto_raw, "tex")
    if not tex:
        tex = re.sub(r"```(latex|tex)?", "", texto_raw).replace("```", "").strip()
    
    tex = re.sub(r"\\documentclass.*", "", tex)
    tex = re.sub(r"\\usepackage.*", "", tex)
    tex = re.sub(r"\\begin\{document\}", "", tex)
    tex = re.sub(r"\\end\{document\}", "", tex)
    return tex.strip()

def guardar_y_procesar_todo(semana_str, prob_id, num_problema, contenido_texto):
    """
    1. Procesa y guarda el script Python, asegurando el guardado del PNG en semana_XX/graficas/
    2. Genera la solución TeX adaptada a IEEE y añade el bloque de figura especificando C = 0.
    """
    carpeta_graficas = os.path.join(f"semana_{semana_str}", "graficas")
    nombre_png = f"{prob_id}_grafica.png"
    
    ruta_png_sistema = os.path.join(carpeta_graficas, nombre_png)
    ruta_png_tex = f"semana_{semana_str}/graficas/{nombre_png}"
    
    # 1. Extraer y procesar script de Python
    codigo_py = extraer_bloque_codigo(contenido_texto, "python")
    
    if codigo_py:
        ruta_png_python = ruta_png_sistema.replace("\\", "/")

        header_matplotlib = (
            "import matplotlib\n"
            "matplotlib.use('Agg')\n"
        )
        if "import matplotlib" not in codigo_py:
            codigo_py = header_matplotlib + codigo_py
        else:
            codigo_py = header_matplotlib + codigo_py

        if "plt.show()" in codigo_py:
            codigo_py = codigo_py.replace("plt.show()", "")

        instruccion_guardado = f"\nplt.savefig(r'{ruta_png_python}', dpi=300, bbox_inches='tight')\nplt.close()\n"
        codigo_py += instruccion_guardado

        ruta_script = os.path.join(carpeta_graficas, f"{prob_id}_grafica.py")
        with open(ruta_script, "w", encoding="utf-8") as f:
            f.write(codigo_py)
        print(f"   🐍 Script Python guardado: {ruta_script}")

        try:
            subprocess.run([sys.executable, ruta_script], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   🖼 Imagen PNG guardada: {ruta_png_sistema}")
        except Exception as e:
            print(f"   ⚠ No se pudo renderizar la imagen PNG: {e}")

    # 2. Limpiar fragmento TeX y anexar la figura adaptada al ancho de columna IEEE con la aclaración de C = 0
    codigo_tex = limpiar_fragmento_tex(contenido_texto)
    
    bloque_figura = f"""\n
\\begin{{figure}}[H]
\t\\centering
\t\\includegraphics[width=\\columnwidth]{{{ruta_png_tex}}}
\t\\caption{{Representación gráfica de $f(x)$ y su antiderivada $F(x)$ evaluada para la constante de integración $C = 0$ (Problema {num_problema}).}}
\t\\label{{fig:problema{num_problema}}}
\\end{{figure}}
"""
    codigo_tex_completo = codigo_tex + bloque_figura

    ruta_solucion = os.path.join(f"semana_{semana_str}", "tex_soluciones", f"{prob_id}_solucion.tex")
    with open(ruta_solucion, "w", encoding="utf-8") as f:
        f.write(codigo_tex_completo)
    print(f"   💾 Archivo LaTeX IEEE guardado: {ruta_solucion}")

def main():
    args = obtener_argumentos()
    num_semana = args.semana
    semana_str = f"{num_semana:02d}"

    json_path = f"banco_problemas/semana_{semana_str}.json"

    print(f"--- Generación para Formato IEEE (Dos Columnas) - Semana {semana_str} ---")
    crear_estructura_directorios(semana_str)
    problemas = cargar_problemas(json_path)

    print(f"Se cargaron {len(problemas)} problemas desde {json_path}.\n")

    system_instruction = (
        "Eres un docente experto en Cálculo Integral. Tu tarea es responder con el desarrollo de un ejercicio "
        "diseñado para ser INCLUIDO DIRECTAMENTE en un documento formato IEEE DE DOS COLUMNAS mediante \\input{}.\n\n"
        "REGLAS STRICTAS PARA DOS COLUMNAS (IEEE):\n"
        "1. NO incluyas preámbulo (NADA de \\documentclass, \\usepackage, o \\begin{document}).\n"
        "2. Empieza directamente con \\subsection*{Problema XX}.\n"
        "3. ECUACIONES CORTAS: El espacio horizontal es estrecho. NUNCA escribas ecuaciones matemáticas muy largas en una sola línea. "
        "Usa el entorno align* o multline* para dividir el desarrollo algebraico en múltiples líneas cortas.\n"
        "4. Usa \\dfrac y fracciona las operaciones paso a paso para evitar que sobrepasen el ancho de columna.\n"
        "5. NO usas marcas Markdown (#, **, ---).\n"
        "6. Escapa los guiones bajos en el texto (ejemplo: \\textbf{Solución:}).\n"
        "7. NO agregues el entorno \\begin{figure} en LaTeX; el script de Python lo insertará escalado a \\columnwidth.\n"
        "8. REGLA DE GRAFICACIÓN: En el script de Python, la curva correspondiente a la antiderivada F(x) DEBE etiquetarse explícitamente en la leyenda indicando C = 0 (ejemplo: label=r'$F(x)$ con $C=0$').\n"
        "9. Devuelve la solución LaTeX en ```latex ... ``` y el script de Python en ```python ... ```."
    )

    for i, prob in enumerate(problemas, start=1):
        prob_id = prob["id"]
        enunciado = prob["enunciado"]
        observaciones = prob["observaciones"]
        num_str = f"{i:02d}"

        print(f"[{i}/{len(problemas)}] Procesando {prob_id} (Problema {num_str})...")

        prompt = (
            f"ID Problema: {prob_id}\n"
            f"Número de Problema para el título: {num_str}\n"
            f"Enunciado: {enunciado}\n"
            f"Indicaciones/Observaciones: {observaciones}\n\n"
            "Resuelve el problema adaptando las ecuaciones al formato estrecho IEEE de 2 columnas e incluye en la leyenda del gráfico que C = 0."
        )

        exito = False

        for model_name in MODELOS_PREFERIDOS:
            if exito:
                break

            max_retries = 3
            for intento in range(max_retries):
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.2
                        )
                    )

                    resultado_texto = response.text
                    guardar_y_procesar_todo(semana_str, prob_id, num_str, resultado_texto)

                    print(f"✓ {prob_id} procesado correctamente usando [{model_name}].\n")
                    exito = True
                    break

                except Exception as e:
                    mensaje_error = str(e)

                    if "429" in mensaje_error:
                        espera = 65
                        print(f"⏳ Cuota llena (429) en {model_name}. Esperando {espera}s...")
                        time.sleep(espera)
                    elif "503" in mensaje_error:
                        espera = 8 * (intento + 1)
                        print(f"⚠️ Servidor ocupado (503) en {model_name}. Esperando {espera}s...")
                        time.sleep(espera)
                    else:
                        print(f"⚠️ Error ({mensaje_error[:100]}). Reintentando en 5s...")
                        time.sleep(5)

            if not exito:
                print(f"🔄 Cambiando de modelo por saturación en {model_name}...")

        if not exito:
            print(f"❌ No se pudo procesar {prob_id}. Saltando...\n")

        time.sleep(10)

    print(f"\n¡Proceso de la Semana {semana_str} finalizado exitosamente!")

if __name__ == "__main__":
    main()