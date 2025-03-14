import os

# Ruta de la carpeta que quieres organizar
carpeta = "C:\\Users\\danahea\\OneDrive - SINOPEC Ecuador\\Desktop\\IT\\ACTAS DE ENTERGA"


# Renombrar archivos
for i, archivo in enumerate(os.listdir(carpeta)):
    nombre_nuevo = f"archivo_{i}.pdf"  # Cambia la extensión según necesites
    os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nombre_nuevo))

print("Archivos renombrados con éxito.")
