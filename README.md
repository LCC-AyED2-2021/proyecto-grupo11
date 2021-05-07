# Proyecto Semestral, Algoritmos II
## Generación de biblioteca virtual para búsquedas de documentos relevantes.

### Objetivos Generales
- Desarrollar una aplicación para manejar una biblioteca virtual de documentos utilizando una estructura de datos previamente definida en la misma aplicación.
- Desarrollar mecanismos eficientes de consultas sobre los documentos de la biblioteca.

### Requerimientos
- Lograr el cumplimiento de los objetivos a través de una aplicación (script) utilizando el lenguaje de programación python3.
- A través de la aplicación desarrollada, permitir la creación de la biblioteca utilizando una dirección local (un directorio del propio ordenador) que contiene los documentos que componen la biblioteca.
- Para la creación de la biblioteca se utilizará el siguiente comando: **python personal_library.py -create <local_path>**
- Una vez cargados los documentos en la aplicación (creación de la biblioteca), permitir realizar consultas sobre el contenido de los documentos en la biblioteca.
- Para la generación de consultas se utilizará el siguiente comando: **python personal_library.py -search <key_word>**
- Para el desarrollo de la aplicación **solamente queda permitido** el uso de algunas estructuras y tipos de datos nativos de python como: array, list, boolean, int y string y la biblioteca math. El resto de las estructuras utilizadas deben ser exclusivamente implementadas por el equipo de trabajo.
- Garantizar la persistencia de los datos. Esto significa que todos los documentos de la biblioteca tienen que ser recuperables a través de consultas en todo momento.
- Los equipos de trabajo deben estar compuestos por 2 estudiantes. No se permiten trabajos individuales y en caso de que el número total de estudiantes sea impar se conformará solamente un equipo de 3 estudiantes.

## Evaluación del proyecto
- Para la evaluación del proyecto entra en consideración los siguientes factores:
    1. Perfecto entendimiento de cada integrante del equipo de todo el código del   proyecto.
    2. Perfecto entendimiento de cada integrante del equipo de los problemas surgidos y soluciones generadas durante toda la fase de desarrollo de la aplicación.
    3. Correcto funcionamiento de la aplicación acorde a los objetivos planteados.
    4. Claridad y documentación del código.
    5. Correcta elección de las estructuras de datos y algoritmos utilizados.
    6. Eficiencia de la aplicación relacionada al costo temporal y espacial.

## Creación de la Biblioteca
- Para la creación de la biblioteca se utilizará el siguiente comando: **python personal_library.py -create <local_path>**
- **<local_path>** representa la dirección local de la carpeta que contiene los documentos de la biblioteca.
- Una vez finalizado el proceso de creación de la biblioteca la aplicación devolverá el texto **“library created successfully”**. A partir de este momento se pueden iniciar las búsquedas.
- La biblioteca deberá persistir la información de manera que se pueda acceder a sus documentos en todo momento. Esto significa que no se deberá volver a crear la biblioteca en cada búsqueda, sino que se realizará sobre una estructura persistente en disco, que se levantará a memoria cada vez que se requiera hacer una consulta.

## Búsquedas de documentos
- La búsqueda de documentos se va a realizar a través de palabras claves. Para ellos se utilizará el comando: **python personal_library.py -search <key_word>**.
- El resultado de una búsqueda a través de una palabra clave **(<key_word>)** va a devolver todos los títulos de los documentos que contienen esa palabra clave en su texto ordenados por relevancia.
- La relevancia se calcula por el número de ocurrencias de la palabra clave en el documento. Los documentos con mayor relevancia irán primero en el resultado de la búsqueda.
- En caso de no existir ningún documento en la biblioteca que contenga la palabra clave se devolverá el texto: **“no document found”**.

## Estructura de la Aplicación a realizar
- Se implementará un script en python utilizando la versión 3. El script tendrá el nombre personal_library.py. Sobre ese script se realizarán las operaciones de creación y búsqueda. El manejo de errores, excepciones y posibles valores de entrada corren a cargo de los desarrolladores de la aplicación. Dicho script será utilizado para realizar las pruebas para evaluar el desempeño de la aplicación.