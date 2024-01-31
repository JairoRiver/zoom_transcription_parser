def save(files_names, history_file):
    # Obtener nombres de ficheros ya presentes en el archivo
    files_procesed = set()
    try:
        with open(history_file, 'r') as file_name_procesed:
            # Lee los nombres de ficheros existentes y los guarda en un conjunto
            files_procesed = set(line.strip() for line in file_name_procesed)
    except FileNotFoundError:
        pass  # Ignora si el archivo aún no existe

    # Abrir el archivo de texto en modo append ('a')
    with open(history_file, 'a') as txt_file:
        # Escribir cada nombre de fichero en una nueva línea
        for file_name in files_names:
            if file_name not in files_procesed:
                txt_file.write(file_name + '\n')