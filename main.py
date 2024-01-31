import os.path
from utils.prepare_doc import prepare_document
from utils.parse_doc import parse_and_save
from utils.read_files import get_files_names
from utils.save_history import save


if __name__ == "__main__":
    all_files = get_files_names('input_docs')
    print(all_files)

    files_procesed = set()
    try:
        with open('docx_procesed.txt', 'r') as file_name_procesed:
            # Lee los nombres de ficheros existentes y los guarda en un conjunto
            files_procesed = set(line.strip() for line in file_name_procesed)
    except FileNotFoundError:
        pass

    for new_file in all_files:
        if new_file not in files_procesed:
            # Ruta al documento "docx"
            input_path_name = os.path.join('input_docs',new_file)

            # Llama a la función para leer el documento
            sections = prepare_document(input_path_name)

            # Parseamos y guardamos el documento final
            output_path_name = os.path.join('output_docs', new_file.split('.')[0] + '_output.docx')
            parse_and_save(sections, output_path_name)
            print(sections[0:2])

    save(all_files, 'docx_procesed.txt')
