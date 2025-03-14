import os
import shutil

# Ruta de la carpeta que quieres organizar
carpeta = "C:\\Users\\danahea\\OneDrive - SINOPEC Ecuador\\Desktop\\IT\\topologia data center"
categorias = {
    "PDFs": [".pdf"],
    "Imágenes": [".jpg", ".png", ".jpeg"],
    "Excels": [".xls", ".xlsx"],
    "Word": [".doc", ".docx"],
    "Otros": []  # Archivos que no coinciden con las anteriores
}

# Crear carpetas si no existen
for categoria in categorias.keys():
    carpeta_destino = os.path.join(carpeta, categoria)
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

# Mover archivos a la carpeta correspondiente
for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, archivo)
    
    # Verificar si es un archivo
    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()  # Obtener extensión
        
        # Buscar en qué categoría encaja
        destino = "Otros"  # Por defecto, carpeta "Otros"
        for categoria, extensiones in categorias.items():
            if extension in extensiones:
                destino = categoria
                break
        
        # Mover archivo
        shutil.move(ruta_archivo, os.path.join(carpeta, destino, archivo))

print("Archivos organizados con éxito. 🎯")
