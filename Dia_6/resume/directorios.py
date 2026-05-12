import os
from pathlib import Path

def abrir_archivo(ruta_archivo):
    archivo = open(ruta_archivo, "r", encoding="utf-8")
    print("Contenido del archivo:")
    for linea in archivo.readlines():
        print(linea.strip())
    archivo.close()

ruta = os.getcwd()  # Obtiene el directorio de trabajo actual
print("Ruta actual:", ruta)

os.chdir("..")
print("Ruta después de cambiar al directorio padre:", os.getcwd())

os.chdir(os.getcwd() + "/python-16-dias/Dia_6/resume")

print("Ruta después de cambiar al directorio resume:", os.getcwd())

ruta_archivo = os.getcwd() + "/file_1.txt"
abrir_archivo(ruta_archivo)

nombre_archivo = os.path.basename(ruta_archivo)
ruta_directorio = os.path.dirname(ruta_archivo)
print("Nombre del archivo:", nombre_archivo)
print("Ruta del directorio:", ruta_directorio)

ruta_completa = os.path.split(ruta_archivo)
print("Ruta completa (directorio, archivo):", ruta_completa)


# Crear directorios en el mismo nivel
os.makedirs("dir_creado", exist_ok=True)  # Crea un directorio llamado "dir_creado" si no existe
print("Directorio 'dir_creado' creado o ya existía.")

os.makedirs("archivos_python", exist_ok=True)  # Crea un directorio llamado "dir_creado" si no existe
print("Directorio 'archivos_python' creado o ya existía.")

# Eliminar directorios en el mismo nivel
os.rmdir("dir_creado")  # Elimina el directorio "dir_creado"
print("Directorio 'dir_creado' eliminado.")



# Path

cwd_path = Path.cwd()  # Obtiene el directorio de trabajo actual como un objeto Path
print("Ruta actual (Path):", cwd_path)

abrir_archivo(cwd_path / "file_2.txt")  # Abre el archivo usando Path