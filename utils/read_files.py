import os

def get_files_names(folder_name):
    # Lista para almacenar los nombres de los ficheros
    files_names = []

    # Obtener la lista de ficheros en la carpeta
    for file_name in os.listdir(folder_name):
        # Agregar el nombre del fichero a la lista
        files_names.append(file_name)

    files_names = [element for element in files_names if element != ".gitkeep"]

    return files_names