import os

def cargar_plantilla(nombre):
    archivos = {
        "Correo AIEP": "aiep.html",
        "Correo Banco": "banco.html",
        "Correo Netflix": "netflix.html"
    }
    archivo = archivos.get(nombre)
    if not archivo:
        return ""
    ruta = os.path.join("html", archivo)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error al cargar la plantilla: {e}")
        return ""
