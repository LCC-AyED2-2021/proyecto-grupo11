## Importar módulos 
import sys
import os
import pickle
from lib.algo1 import *
from lib import linkedlist
from lib.strcmpAlt import strcmpAlt
from lib import trie

## Switch debug log
logging = False

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
    if lista!=None: #Si la lista existe
        lista=trie.InsertionSort(lista.head) #Se llama a InsertionSort para ordenarla de mayor a menor
        while lista != None: #Se recorre la lista y se imprime
            print(lista.value,": ", end="")
            print(lista.key, " ocurrencias.")
            lista=lista.nextNode
    else: #Si no existe la lista
        print("no document found") #Se le avisa al usuario de que no se encuentra la palabra en los documentos


## Definimos funciones auxiliares
#         ---Create---

# Esto copia los títulos de los textos que están en la carpeta que tiene el local_path, despues abre cada documento, los lee y inserta cada palabra en nuestra estructura que pensamos
def crear_estructura(local_path):

    # voy a trabajar con string de python cuando uso funciones de os porque estas no me deja trabajar con String()

    estructura = trie.Trie()

    lista_documentos = os.listdir(local_path)
    if logging:
        print("Lista de documentos en este path:")
        for i in range(len(lista_documentos)):
            print(lista_documentos[i])

    # Nota: se usa una lista de python porque es lo que devuelve listdir, esta puede ser usada similar a un array en donde
    # tenemos subindices, en este caso en particular cada subindice va a tener un titulo de un documento

    # Acá abrimos los documentos
    for documentos in range(0, len(lista_documentos)):
        if logging: print("Procesando texto ", documentos, " ...")
        path_documento_a_leer = local_path + "/" + lista_documentos[documentos]

        leer_palabras(lista_documentos[documentos], path_documento_a_leer, estructura)

    # Retornar la estructura creada
    return estructura

# Lee cada palabra del documento y la inserta en la estructura
def leer_palabras(documento, path_documento, estructura):

    with open(path_documento, encoding="utf8") as documento_a_leer:  # Abre el documento y lee linea por linea (se usa la opción UTF-8 para no tener problemas con cierto caracteres)
        lineas = documento_a_leer.readlines()  # Nota: lineas tiene dos parametros porque el primero es la linea en donde estamos del documento y el segundo es la letra en donde estamos de la linea
        palabra = String("")  # Empezamos la variable palabra con una string vacía
        palabra_vacia = True
        for i in range(0, len(lineas)):  # Recorremos todas las lineas del documento
            for j in range(0, len(lineas[i])):  # Recorremos todos los caracteres de la linea
                if not caracteres_separadores(lineas[i], j):  # Si el caracter en donde estamos no es ninguno de los caracteres que separa palabras o que no sirve a formar palabras entonces lo agregamos a la palabra
                    palabra_vacia = False
                    palabra = concat(palabra, String(lineas[i][j]))

                    if j == len(lineas[i]) - 1: #si estamos en el ultimo caracter y este no es un caracter separador para evitar saltar la ultima palabra de un documento la insertamos en la estructura acá
                        ultimo_nodo_trie = trie.insert(estructura, palabra)  # El insert retornará el ultimo nodo correspondiente a la palabra en el Trie
                        actualizar_docsWhereApears(ultimo_nodo_trie, documento)
                        palabra = String("")
                        palabra_vacia = True
                else:  # Sino insertamos la palabra que obtuvimos hasta este punto y resteamos la variable palabra
                    if not palabra_vacia: #este if sirve para que cuando haya 2 o más caracteres separadores o que ignoramos seguidos no inserta la palabra vacia como palabra en la estructura
                        ultimo_nodo_trie = trie.insert(estructura, palabra)  # El insert retornará el ultimo nodo correspondiente a la palabra en el Trie
                        actualizar_docsWhereApears(ultimo_nodo_trie, documento)
                        palabra = String("")
                        palabra_vacia = True


# Funcion que nos dice si un caracter pertenece al conjunto de caracteres que no nos interesan para formar palabras (como por ejemplo un espacio vacio)
def caracteres_separadores(linea, j):
    # caracteres que ignoramos siempre porque no nos sirven para formar palabras o otras cosas utiles 
    #  + = () [] {} < > : ; ? ! / \ | " # & * • ‘ “ ” ´ © → @ ˆ ^ ` † … ∈ ~ ≥

    caracter = linea[j]
    if strcmp(caracter, String(" ")) or strcmp(caracter, String("(")) or strcmp(caracter, String(")")) or strcmp(caracter, String("[")) or strcmp(caracter, String("]")) or strcmp(caracter, String("{")) or strcmp(caracter, String("}"))or strcmp(caracter, String("<")) or strcmp(caracter, String(">")) or strcmp(caracter, String("+")) or strcmp(caracter, String("=")) or strcmp(caracter, String("*")) or strcmp(caracter, String("/")) or strcmp(caracter, String("\\")) or strcmp(caracter, String("|")) or strcmp(caracter, String("©")) or strcmp(caracter, String("#")) or strcmp(caracter, String("@")) or strcmp(caracter, String("&")) or strcmp(caracter, String(";")) or strcmp(caracter, String(":")) or strcmp(caracter, String("?")) or strcmp(caracter, String("!")) or strcmp(caracter, String('"')) or strcmp(caracter, String('‘')) or strcmp(caracter, String('•')) or strcmp(caracter, String('“')) or strcmp(caracter, String('”')) or strcmp(caracter, String('´')) or strcmp(caracter, String("→")) or strcmp(caracter, String("ˆ")) or strcmp(caracter, String("^")) or strcmp(caracter, String("`")) or strcmp(caracter, String("†")) or strcmp(caracter, String("…")) or strcmp(caracter, String("∈")) or strcmp(caracter, String("~")) or strcmp(caracter, String("≥")) or caracter == "\n":
        return True
    else:
        # casos especiales que necesitan un poco más de procesamiento para decir si son saltables o no

        caracter_anterior_ooi = False
        caracter_posterior_ooi = False
        #estos dos ifs son para que no se vaya out of index
        if j - 1 > 0:
            caracter_anterior = linea[j-1]
        else:
            caracter_anterior_ooi = True #ooi == out of index
        if j + 1 < len(linea):
            caracter_posterior = linea[j+1]
        else:
            caracter_posterior_ooi = True

        if strcmp(caracter, String("-")) or strcmp(caracter, String("−")) or strcmp(caracter, String("—")): # -−— palabras inglesas con guion y numeros negativos
            if not caracter_anterior_ooi and not caracter_posterior_ooi:
                if ascii_mayuscula(caracter_anterior) >= 65 and ascii_mayuscula(caracter_anterior) <= 90 and ascii_mayuscula(caracter_posterior) >= 65 and ascii_mayuscula(caracter_posterior) <= 90:  # Si el caracter anterior y posterior son letras del alfabeto entonces decidimos que esta es una palabra especial en ingles compuesta por dos palabras y un guion en el medio (65 y 90 son los limites de las letras mayusculas en la tabla ascii, revisamos solo esas porque ascii_mayuscula transforma las minusculas en mayusculas)
                    return False
                elif not caracter_posterior_ooi: #si tenemos un caracter posterior nos fijamos que no sea un numero negativo
                    if ord(caracter_posterior) <= 57 and ord(caracter_posterior) >= 48: # Si el caracter posterior es un numero entonces decidimos que este es un numero negativo (48 y 57 son los limites de los numeros en la tabla ascii):
                        return False
                    else: # Si a la derecha no tiene numeros entonces podria ser un menos, entonces no nos sirve para formar palabras
                        return True  
                else: # Si a los costados no tiene letras entonces podria ser un menos, entonces no nos sirve para formar palabras
                    return True
            elif not caracter_posterior_ooi: #si tenemos un caracter posterior nos fijamos que no sea un numero negativo
                if ord(caracter_posterior) <= 57 and ord(caracter_posterior) >= 48: # Si el caracter posterior es un numero entonces decidimos que este es un numero negativo (48 y 57 son los limites de los numeros en la tabla ascii):
                    return False
                else: # Si a la derecha no tiene numeros entonces podria ser un menos, entonces no nos sirve para formar palabras
                    return True  
            else: # si no tenemos los dos caracteres anterior y posterior en este caso podemos decir directamente que es un caracter que no nos sirve porque para ser el caso especial necesita los dos caracteres
                return True
        elif strcmp(caracter, String(".")) or strcmp(caracter, String(",")): # . , numeros con coma
            if not caracter_anterior_ooi and not caracter_posterior_ooi:
                if ord(caracter_anterior) <= 57 and ord(caracter_anterior) >= 48 and ord(caracter_posterior) <= 57 and ord(caracter_posterior) >= 48: # Si el caracter anterior y posterior son numeros entonces decidimos que este es un numero con coma (48 y 57 son los limites de los numeros en la tabla ascii)
                    return False
                else: # Si a los costados no tiene numeros entonces podria ser un punto o una coma normal, entonces no nos sirve para formar palabras
                    return True
            else: # si no tenemos los dos caracteres anterior y posterior en este caso podemos decir directamente que es un caracter que no nos sirve porque para ser el caso especial necesita los dos caracteres
                return True 
        elif strcmp(caracter, String("'")) or strcmp(caracter, String("’")): # ' ’ palabras inglesas con apostrofe
            if not caracter_anterior_ooi:
                if buscar_caracter_en_palabra(String("'"),linea, j) or buscar_caracter_en_palabra(String("‘"),linea, j): #si existe otro apostrofe que lo cierra entonces lo estamos usando como comillas, las que no nos sirven para crear palabras
                    return True
                elif ascii_mayuscula(caracter_anterior) >= 65 and ascii_mayuscula(caracter_anterior) <= 90: #si ademas de no tener otro apostrofe en la palabra como minimo tenemos una letra a la izquierda entonces la podemos considerar como util para formar una palabra en ingles (cosas como can't y el genitivo sajón)
                    return False
                else: #si no tiene una letra a la izquierda no es un palabra en ingles y podria ser un apostrofe solo
                    return True
            else: # si no tenemos el caracteres anterior en este caso podemos decir directamente que es un caracter que no nos sirve porque para ser el caso especial lo necesita
                return True
            

        return False #si el caracter no corresponde a ninguno de estos casos especiales devolvemos False

# Este algoritmo nos dice si existe un caracter en la palabra en la que estamos analizando usando tambien el codigo de caracteres separadores para saber donde empieza y termina (ademas revisa tambien la parte que todavia no analizamos)
def buscar_caracter_en_palabra(caracter_a_buscar, linea, j): 

    i = j - 1
    while i > 0: #revisamos la izquierda hasta llegar al limite de la linea o hasta llegar a un caracter separador (break más abajo)
        if strcmp(linea[i], caracter_a_buscar): #si encontramos el caracter que buscabamos entonces devolvemos true
            return True

        if caracteres_separadores(linea, i): #esto se revisa despues porque si lo hacemos antes podria suceder un bucle infinito
            break
        i = i - 1

    i = j + 1
    while i < len(linea): #revisamos la derecha hasta llegar al limite de la linea o hasta llegar a un caracter separador (break más abajo)
        if strcmp(linea[i], caracter_a_buscar): #si encontramos el caracter que buscabamos entonces devolvemos true
            return True

        if caracteres_separadores(linea, i): #esto se revisa despues porque si lo hacemos antes podria suceder un bucle infinito
            break
        i = i + 1

    return False #si despues de haber revisado la izquierda y la derecha de la palabra no encontramos nada entonces devolvemos False

# Funcion que si recibe una letra minuscula la transforma en ascii de letra mayuscula, sino convierte simplemente en ascii
def ascii_mayuscula(caracter):

    codigo_original = ord(caracter)
    corrector = 0

    if codigo_original >= 97 and codigo_original <= 122:
        corrector = 32

    # Calcular el codigo final
    codigoFinal = codigo_original - corrector

    # Retornar el codigo final
    return codigoFinal

# Este función es llamada despues de insertar una palabra a la estructura. Actualizará el campo docsWhereApears de la palabra insertada. Recibe por parametro el ultimo nodo de la palabra dentro de la estructura
def actualizar_docsWhereApears(nodo, documento):
    if nodo.docsWhereApears != None: #Si la lista existe
        if nodo.docsWhereApears.head.value != documento: #Si estamos trabajando con un documento distinto
            linkedlist.add(nodo.docsWhereApears, documento, 1)  #Se agrega el documento a la lista
        else: #Si se trabaja con el mismo
            nodo.docsWhereApears.head.key = nodo.docsWhereApears.head.key + 1 #Se aumenta una aparicion de la palabra en el documento
    else: #Si la lista no existe
        nodo.docsWhereApears=linkedlist.LinkedList() #Se define
        linkedlist.add(nodo.docsWhereApears, documento, 1)   #Y se agrega el documento, al inicio de la lista

### Código __main__ ###
# Leer los argumentos pasados por consola, verificar y ejecutar funciones
if len(sys.argv) == 3:
    if strcmpAlt(String(sys.argv[1]), String('-create')):
        # Ejecutar '-create'
        create(sys.argv[2])
    elif strcmpAlt(String(sys.argv[1]), String('-search')):
        # Ejecutar '-search'
        search(sys.argv[2])
    else:
        print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
