from docx import Document
import re

def is_int(cadena):
    # Define el patrón de expresión regular para un entero
    int_pattern = r'^[+-]?\d+$'

    # Utiliza re.match para verificar si la cadena coincide con el patrón
    coincide = re.match(int_pattern, cadena)

    # Retorna True si coincide, False en caso contrario
    return bool(coincide)


def is_time_format(cadena):
    # Define el patrón de expresión regular para el formato de tiempo
    time_pattern = r'^\d{2}:\d{2}:\d{2}.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}.\d{3}$'

    # Utiliza re.match para verificar si la cadena coincide con el patrón
    coincide = re.match(time_pattern, cadena)

    # Retorna True si coincide, False en caso contrario
    return bool(coincide)

def prepare_document(docx_path):
    # Abre el documento
    doc = Document(docx_path)

    n = 0
    sections = []
    section = {}

    # Separamos el documentos en parrafos de la transcripción
    # Itera sobre los párrafos en el documento
    for paragraph in doc.paragraphs:
        # Omintimos la cabecera
        if n == 0:
            n += 1 
            continue

        if len(paragraph.text) == 0 and len(section) > 0:
            sections.append(section)
            section = {}
            n += 1
            continue

        if is_int(paragraph.text):
            section["id"] = paragraph.text
            n += 1
            continue

        if is_time_format(paragraph.text):
            section["time"] = paragraph.text
            n += 1
            continue

        if len(paragraph.text) > 0:
            section["transcription"] = paragraph.text
            n += 1
            continue

        if n == 10 : break
        n += 1
    return sections