## Importar módulos 
from lib import linkedlist
from lib.linkedlist import LinkedList, add
import sys
import os
import pickle
from lib import algo1
from lib import trie
from lib import strcmpAlt as sc

## Definir funciones principales

def create(local_path):
    if os.path.exists(local_path):  # Nos fijamos si la path que nos pasó el usuario existe, si existe continuamos con el algoritmo
        biblioteca = crear_estructura(local_path)   # Creamos el archivo de la biblioteca en binario y escribimos la estructura que hicimos dentro de ella
        with open("biblioteca.bin", "bw") as crear_biblioteca:
            pickle.dump(biblioteca, crear_biblioteca)
            print("library created successfully")

    else:  # Sino mandamos un error
        print("Error: No se encontró el path indicado")



def search(palabra):
    biblioteca=None
    with open("biblioteca.bin", "br") as leer_biblioteca:
        biblioteca=pickle.load(leer_biblioteca)
    lista=trie.getWord(biblioteca,palabra)
    lista=trie.InsertionSort(lista.head)
    while lista.nextNode!=None:
        print(lista.value,":", end="")
        print(lista.key, ",", end="")
        lista=lista.nextNode
    return True


## Definimos funciones auxiliares
#         ---Create---

# Lee cada palabra del documento y la inserta en la estructura
def leer_palabras(documento, estructura):

    with open(documento, encoding="utf8") as documento_a_leer:  # Abre el documento y lee linea por linea (se usa la opción UTF-8 para no tener problemas con cierto caracteres)
        lineas = documento_a_leer.readlines()  # Nota: lineas tiene dos parametros porque el primero es la linea en donde estamos del documento y el segundo es la letra en donde estamos de la linea
        palabra = algo1.String("")  # Empezamos la variable palabra con una string vacía
        palabra_vacia = True
        for i in range(0, len(lineas)):  # Recorremos todas las lineas del documento
            for j in range(0, len(lineas[i])):  # Recorremos todos los caracteres de la linea
                if not caracteres_separadores(lineas[i][j]):  # Si el caracter en donde estamos no es ninguno de los caracteres que separa palabras o que no sirve a formar palabras entonces lo agregamos a la palabra
                    palabra_vacia = False
                    palabra = algo1.concat(palabra, algo1.String(lineas[i][j]))
                else:  # Sino insertamos la palabra que obtuvimos hasta este punto y resteamos la variable palabra
                    if not palabra_vacia: #este if sirve para que cuando haya 2 o más caracteres separadores o que ignoramos seguidos no inserta la palabra vacia como palabra en la estructura
                        ultimo_nodo_trie = trie.insert(estructura, palabra)  # El insert retornará el ultimo nodo correspondiente a la palabra en el Trie
                        # TODO: aca incrementar el valor de esta palabra correspondiente al doc actual.
                        ''' Pseudocodigo
                        if ultimo_nodo_tire.docsWhereApears.head != documento:
                            LinkedList.add(ultimo_nodo_tire.docsWhereApears.head, (documento,1)) #  Como tupla, o array
                        else: ## Ya existe en el documento, solo incrementar
                            old = ultimo_nodo_tire.docsWhereApears.head
                            old = old+1
                        '''
                        if ultimo_nodo_trie.docsWhereApears != None:
                            if ultimo_nodo_trie.docsWhereApears.head.value != documento:
                                linkedlist.add(ultimo_nodo_trie.docsWhereApears, documento, 1)
                            else:
                                ultimo_nodo_trie.docsWhereApears.head.key = ultimo_nodo_trie.docsWhereApears.head.key + 1
                        else:
                            ultimo_nodo_trie.docsWhereApears=linkedlist.LinkedList()
                            linkedlist.add(ultimo_nodo_trie.docsWhereApears, documento,1)   
                        palabra = algo1.String("")
                        palabra_vacia = True


# Funcion que nos dice si un caracter pertenece al conjunto de caracteres que no nos interesan para formar palabras (como por ejemplo un espacio vacio)
def caracteres_separadores(caracter):

    # + - =  () [] {} . , : ; ? ! / " # *
    # casos especiales (TODAVIA NO LOS PROGRAME)
    # - guion como una sola palabra, si esta solo entonces no porque seria un menos
    # numeros con coma
    # caso especial ' o ’
    # emails
    # urls ?
    if algo1.strcmp(caracter, algo1.String(" ")) or algo1.strcmp(caracter, algo1.String("(")) or algo1.strcmp(caracter, algo1.String(")")) or algo1.strcmp(caracter, algo1.String("[")) or algo1.strcmp(caracter, algo1.String("]")) or algo1.strcmp(caracter, algo1.String("{")) or algo1.strcmp(caracter, algo1.String("}")) or algo1.strcmp(caracter, algo1.String("+")) or algo1.strcmp(caracter, algo1.String("=")) or algo1.strcmp(caracter, algo1.String("*")) or algo1.strcmp(caracter, algo1.String("/")) or algo1.strcmp(caracter, algo1.String("@")) or algo1.strcmp(caracter, algo1.String("#")) or algo1.strcmp(caracter, algo1.String("&")) or algo1.strcmp(caracter, algo1.String(".")) or algo1.strcmp(caracter, algo1.String(",")) or algo1.strcmp(caracter, algo1.String(";")) or algo1.strcmp(caracter, algo1.String(":")) or algo1.strcmp(caracter, algo1.String("?")) or algo1.strcmp(caracter, algo1.String("!")) or algo1.strcmp(caracter, algo1.String('"')) or caracter == "\n":
        return True
    else:
        return False


def crear_estructura(local_path):
    # Esto copia los títulos de los textos que están en la carpeta que tiene el local_path, despues abre cada documento, los lee y inserta cada palabra en nuestra estructura que pensamos
    # voy a trabajar con string de python cuando uso funciones de os porque estas no me deja trabajar con String()

    estructura = trie.Trie()

    # Nota: se cambian todas las "\" a "/" del path porque sino da error
    print("Lista de documentos en este path:")
    lista_documentos = os.listdir(local_path)

    print(lista_documentos)
    # Nota: se usa una lista de python porque es lo que devuelve listdir, esta puede ser usada similar a un array en donde
    # tenemos subindices, en este caso en particular cada subindice va a tener un titulo de un documento

    # Acá abrimos los documentos
    for documentos in range(0, len(lista_documentos)):
        print("Texto: ", documentos)
        documento_a_leer = local_path + "/" + lista_documentos[documentos]

        leer_palabras(documento_a_leer, estructura)

    # Retornar la estructura creada
    return estructura


### Código __main__ ###
# Leer los argumentos pasados por consola, verificar y ejecutar funciones
if len(sys.argv) == 3:
    if sc.strcmpAlt(algo1.String(sys.argv[1]), algo1.String('-create')):
        # Ejecutar '-create'
        create(sys.argv[2])
    elif sc.strcmpAlt(algo1.String(sys.argv[1]), algo1.String('-search')):
        # Ejecutar '-search'
        search(sys.argv[2])
    else:
        print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
