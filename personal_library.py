import sys
import os
import pickle
from lib import algo1 
from lib import trie

# Definir funciones principales

def create(local_path):

    if os.path.exists(local_path): #nos fijamos si la path que nos pasó el usuario existe, si existe continuamos con el algoritmo

        biblioteca= crear_estructura(local_path)
        with  open("biblioteca.txt", "bw") as crear_biblioteca: #creamos el archivo de la biblioteca en binario y escribimos la estructura que hicimos dentro de ella
            pickle.dump(biblioteca, crear_biblioteca)
    else: #sino mandamos un error
        print("Error no se encontró el path indicado")

    print("library created successfully")
    return True


def search():
    return True

# Definimos funciones auxiliares para create y search

def leer_palabras(documento, estructura): #lee cada palabra del documento y la inserta en la estructura

    with open(documento, encoding="utf8") as documento_a_leer: #abre el documento y lee linea por linea (se usa la opcion utf8 para no tener problemas con cierto caracteres)
        #nota: lineas tiene dos parametro porque el primero es la linea en donde estamos del documento y el segundo es la letra en donde estamos de la linea
        
        lineas = documento_a_leer.readlines()
        palabra = algo1.String("") #empezamos la variable palabra con una string vacia
        for i in range(0, len(lineas)):#recorremos todas las lineas del documento

            if i != len(lineas)-1: #esto se hace porque cuando llegamos a la ultima linea no vamos a tener un \n el cual normalmente se encuentra al final de una linea y hace una comparacion más innecesaria
                
                for j in range(0, len(lineas[i])-1): #recorremos todos los caracteres del documento
                    if not caracteres_separadores(lineas[i][j]): #si el caracter en donde estamos no es ninguno de los caracteres que separa palabras o que no sirve a formar palabras entonces lo agregamos a la palabra
                        palabra = algo1.concat(palabra, algo1.String(lineas[i][j]))
                    else: #sino insertamos la palabra que obtuvismo hasta este punto y reseteamos la variable palabra
                        trie.insert(estructura, palabra)
                        palabra = algo1.String("")
            else: #estamos en la ultima linea

                for j in range(0, len(lineas[i])):
                    if not caracteres_separadores(lineas[i][j]):
                        palabra = algo1.concat(palabra, algo1.String(lineas[i][j]))
                    else:
                        trie.insert(estructura, palabra)
                        palabra = algo1.String("")

    return estructura

def caracteres_separadores(caracter): #funcion que nos dice si un caracter pertenece al conjunto de caracteres que no nos interesan para formar palabras (como por ejemplo un espacio vacio)

    # + - =  () [] {} . , : ; ? ! / " # *
    # casos especiales (TODAVIA NO LOS PROGRAME)
    # - guion como una sola palabra, si esta solo entonces no porque seria un menos
    # numeros con coma
    # caso especial ' o ’ 
    # emails
    # urls ?
    if algo1.strcmp(caracter, algo1.String(" ")) or algo1.strcmp(caracter, algo1.String("(")) or algo1.strcmp(caracter, algo1.String(")")) or algo1.strcmp(caracter, algo1.String("[")) or algo1.strcmp(caracter, algo1.String("]")) or algo1.strcmp(caracter, algo1.String("{")) or algo1.strcmp(caracter, algo1.String("}")) or algo1.strcmp(caracter, algo1.String("+")) or algo1.strcmp(caracter, algo1.String("=")) or algo1.strcmp(caracter, algo1.String("*")) or algo1.strcmp(caracter, algo1.String("/")) or algo1.strcmp(caracter, algo1.String("@")) or algo1.strcmp(caracter, algo1.String("#")) or algo1.strcmp(caracter, algo1.String("&")) or algo1.strcmp(caracter, algo1.String(".")) or algo1.strcmp(caracter, algo1.String(",")) or algo1.strcmp(caracter, algo1.String(";")) or algo1.strcmp(caracter, algo1.String(":")) or algo1.strcmp(caracter, algo1.String("?")) or algo1.strcmp(caracter, algo1.String("!")) or algo1.strcmp(caracter, algo1.String('"')):
        return True
    else:
        return False

def crear_estructura(local_path):        
    #Esto copia los titulos de los textos que estan en la carpeta que tiene el local_path, despues abre cada documento, los lee y inserta cada palabra en nuestra estructura que pensamos
    #voy a trabajar con string de python cuando uso funciones de os porque estas no me deja trabajar con String()
    
    estructura = trie.Trie()

    #nota: se cambian todas las "\" a "/" del path porque sino da error
    print("Lista de documentos en este path:")
    lista_documentos = os.listdir(local_path)

    print(lista_documentos)
    #nota: se usa una lista de python porque es lo que devuelve listdir, esta puede ser usada similar a un array en donde
    #tenemos subindices, en este caso en particular cada subindice va a tener un titulo de un documento

    #acá abrimos los documentos
    for documentos in range(0, 4):
        print("Texto: ",documentos)
        documento_a_leer = local_path + "/" + lista_documentos[documentos]

        leer_palabras(documento_a_leer, estructura)

    return estructura


# Leer los argumentos pasados por consola, verificar y ejecutar funciones

if len(sys.argv) == 3:
    if sys.argv[1] == '-create':
        # Ejecutar '-create'
        create(sys.argv[2])
    elif sys.argv[1] == '-search':
        # Ejecutar '-search'
        search()
    else:
        print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')

# Test
## INFO: Implementé la estructura, usando trie.insert(Trie, cadena) se insertará en el trie (con hash tables y todo eso).
# Esta funcion retorna el puntero del nodo correspondiente a la ultima letra (En este caso 'A'),
# de ahi tenemos acceso a el atributo docsWhereApears.

T = trie.Trie()
nodoDePalabraInsertada = trie.insert(T, 'Hola')

print(nodoDePalabraInsertada)
print(nodoDePalabraInsertada.key) # Estoy guardando como key el resultado de lib.latinHash(), ahi mismo dice como lo calcula
print(nodoDePalabraInsertada.docsWhereApears)
print(nodoDePalabraInsertada.children)