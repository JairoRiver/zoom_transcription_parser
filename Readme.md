# ZOOM transcription parser

El objetivo de este script es parsear la salida de las transcripciones de ZOOM a un formato más natural

El fichero de entrada está en formato "docx"

Estructura de la transcripción:

- Cabecera (omitimos)

- 1 (Numeración del parafo, Omitir)

- 00:00:02.070 --> 00:00:25.769 (Marca de tiempo, duración del audio que se va a transcribir, Omitir) 

- Interlocutor_1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas lectus nulla, tincidunt at mauris in, suscipit fringilla nisl. Morbi facilisis massa felis, id molestie velit pulvinar in. Nulla arcu arcu, luctus vitae elit a, fermentum convallis nisl. Integer dignissim elit metus, sit amet mattis purus iaculis a. Praesent rutrum euismod lectus, lobortis tincidunt magna rhoncus nec. (Transcripción, nos quedamos con esta parte)

## Forma de uso
Si tenemos Anaconda como interprete de Python:
- Creamos un entorno virtual
~~~
conda create -n venv
conda activate venv
~~~

- Instalamos las dependencias necesarias
~~~
conda install --file requirements.txt
~~~

- Subimos todos los ficheros que queramos procesar en la carpeta "input_docs", el fomato de los ficheros debe de ser .docx

- Ejecutamos el script:
~~~
python main.py
~~~

- Guardamos una registro de los ficheros procesados en el documento "docx_procesed.txt"

- Si un fichero ya ha sido procesado y volvemos a ejecutar el script, no se volverá a procesar, si queremos que se procese otra vez devemos borrar el nombre del fichero del archivo "docx_procesed.txt"