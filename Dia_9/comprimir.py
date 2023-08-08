# import zipfile
import shutil

# mi_zip = zipfile.ZipFile('arch_comprimido.zip', 'w')
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')
#
# mi_zip.close()


# zip_abierto = zipfile.ZipFile('arch_comprimido.zip', 'r')
#
# zip_abierto.extractall()

# carpeta_origen = '/home/alexth/PycharmProjects/PythonTotal_16_Dias/Dia_6/Proyecto'
# archivo_destino = 'Todo_Comprimido'
#
# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_Comprimido.zip', 'extraccion_terminada', 'zip')


