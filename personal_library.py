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
T = trie.Trie
nodoDePalabraInsertada = trie.insert(T, 'Hola')

print(nodoDePalabraInsertada)
print(nodoDePalabraInsertada.key) # Estoy guardando como key el resultado de lib.latinHash(), ahi mismo dice como lo calcula
print(nodoDePalabraInsertada.docsWhereApears)
print(nodoDePalabraInsertada.children)

# Test fuerza bruta
for i in range(100_000):
    trie.insert(T, str(i))

# Estoy pensando en crear una estructura que simplifique la cantidad de elementos, ya que por cada nodo se hace este camino:
# trie.trieNode.children.array[i].linkedlist.dictionaryNode.trieNode
# Capaz simplificarlo en una sola clase que cumpla de linkedlist, dictionaryNode y trieNode
# Sea como sea, esto lo estoy implementando en los proximos dias. De todas maneras, la funcion trie.insert siempre les va a devolver
# el pointer de la ultima palabra, que es lo que se necesita para modificar el docsWhereApears.
# Cualquier cosa me dicen