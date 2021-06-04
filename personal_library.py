import sys

# Leer los argumentos pasados por consola, verificar y ejecutar funciones

if len(sys.argv) == 3 and False:
    if sys.argv[1] == '-create':
        # Ejecutar '-create'
        create()
    elif sys.argv[1] == '-search':
        # Ejecutar '-search'
        search()
    else:
        print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')
else:
    print(f'Los argumentos dados no son válidos.\nUtilice "-create <local_path>" o "-search <key_word>"')


# Definir funciones principales

def create():
    return True


def search():
    return True

# Test
## INFO: Implementé la estructura, usando trie.insert(Trie, cadena) se insertará en el trie (con hash tables y todo eso).
# Esta funcion retorna el puntero del nodo correspondiente a la ultima letra (En este caso 'A'),
# de ahi tenemos acceso a el atributo docsWhereApears.


from lib import trie
T = trie.Trie()
nodoDePalabraInsertada = trie.insert(T, 'Hola')

print(nodoDePalabraInsertada)
print(nodoDePalabraInsertada.key) # Estoy guardando como key el resultado de lib.latinHash(), ahi mismo dice como lo calcula
print(nodoDePalabraInsertada.docsWhereApears)
print(nodoDePalabraInsertada.children)

#Esto copia los titulos de los textos que estan en una carpeta, despues abre cada documento y los lee para despues printearlos
#voy a trabajar con string de python porque listdir no me deja trabajar con String()

camino= "archivosTest"
#nota: se cambian todas las "\" a "/" del path porque sino da error

lista_documentos= os.listdir(camino)

print(lista_documentos)
#nota: se usa una lista de python porque es lo que devuelve listdir, esta puede ser usada similar a un array en donde
#tenemos subindices, en este caso en particular cada subindice va a tener un titulo de un documento

#acá abrimos los 3 documentos
for documento in range(0, 3):
    print("Texto: ",documento)
    documento_a_leer = open(camino + "/" + lista_documentos[documento], encoding="utf8" )

    contenido_documento = documento_a_leer.read()
    print(contenido_documento)

