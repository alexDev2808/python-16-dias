from pathlib import Path

ruta_archivo = Path(__file__).parent / "file_1.txt"
if ruta_archivo.exists(): # Verifica si el archivo existe
    print(ruta_archivo.name)  # Imprime el nombre del archivo
    print(ruta_archivo.parent)  # Imprime el directorio padre del archivo
    print(ruta_archivo.suffix)  # Imprime la extensión del archivo
    print(ruta_archivo.stem)  # Imprime el nombre del archivo sin la extensión
    print(ruta_archivo.read_text(encoding="utf-8"))  # Lee el contenido del archivo como texto con encoding UTF-8
else:
    print(f"El archivo {ruta_archivo} no existe.")


current_dir = Path.cwd()  # Obtiene el directorio de trabajo actual
base_dir = Path().home()  # Obtiene el directorio home del usuario
print(f"Directorio actual: {current_dir}")
print(f"Directorio home: {base_dir}")

guia = Path(current_dir, "spain", "barcelona", "guia.txt")
print(guia)  # Imprime la ruta completa del archivo guia.txt

guia2 = guia.with_name("guia2.txt")  # Cambia el nombre del archivo a guia2.txt
print(guia2)  # Imprime la nueva ruta con el nombre cambiado

# Crear directorios y archivos
ruta_viajes = current_dir / "Dia_6" / "resume" / "Viajes"
ruta_viaje_esp = ruta_viajes / "Spain" / "Barcelona"
ruta_viaje_fr = ruta_viajes / "France" / "Paris"

ruta_viajes.mkdir(exist_ok=True)  # Crea el directorio "Viajes" si no existe
ruta_viaje_esp.mkdir(parents=True, exist_ok=True)  # Crea el directorio para el viaje a España
ruta_viaje_fr.mkdir(parents=True, exist_ok=True)  # Crea el directorio para el viaje a Francia

viajes_notas = ruta_viajes / "notas.txt"
viajes_notas.write_text("Notas de mis viajes", encoding="utf-8")  # Escribe texto en el archivo notas.txt para los viajes
guia_esp_1 = ruta_viaje_esp / "guia.txt"
guia_esp_1.write_text("Guía de viaje a Barcelona", encoding="utf-8")  # Escribe texto en el archivo guia.txt para España
guia_fr_1 = ruta_viaje_fr / "guia.txt"
guia_fr_1.write_text("Guía de viaje a París", encoding="utf-8")  # Escribe texto en el archivo guia.txt para Francia

for txt in ruta_viajes.glob("**/*.txt"):  # Busca todos los archivos .txt en el directorio Viajes y sus subdirectorios
    print(txt)  # Imprime la ruta de cada archivo encontrado

