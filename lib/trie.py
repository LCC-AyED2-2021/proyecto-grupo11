########
# Esta implementación esta modificada para trabajar con TrieNodes especiales,
# que poseen un atributo (docsWhereApears) que corresponde a una linked list, con los nombres
# de los documentos donde la palabra aparece, y cuantas veces aparece.
########

from lib.latinHash import latinHash as LHash
import lib.algo1 as algo

# Longitud del diccionario sqrt(61) (ascii 7-bits, latin basico sin diferenciar mayúsculas de minúsculas)
m = 8
A = ((5**.5 - 1)/2)  # Golden ratio φ

# Definir clases


class Trie:
    root = None


class TrieNode:
    nextTrieNode = None  # Analogo a un nodo de una linked list
    children = None
    key = None
    docsWhereApears = None

# Definir funciones


def insert(trie, text):
    '''
    Explicación:
        Inserta un elemento en el Trie dado.
    Parametros:
        trie: El Trie en donde se insertará el elemento.
        text: La palabra a insertar. (string)
    Return:
        El puntero del nodo de la ultima letra de la palabra insertada.
    '''
    # Caso Trie no inicializado
    if not trie.root:
        # Se inicializa, children es una hash table
        trie.root = TrieNode()
        trie.root.children = algo.Array(m, TrieNode())

    # Comparar cada nivel del trie con el indice actual de text
    nivelActual = trie.root

    for i in range(0, len(text)):
        # Buscar el caracter en el nivel actual
        caracter = LHash(text[i])
        hashCaracter = h(caracter)

        # Buscar como si fuese una LList el caracter en las colisiones del diccionario.
        nodoDelCaracter = None
        nodoActual = nivelActual.children[hashCaracter]
        while nodoActual:
            if nodoActual.key == caracter:
                nodoDelCaracter = nodoActual
                break
            else:
                nodoActual = nodoActual.nextTrieNode

        # Verificar si ese caracter ya existía, sino se lo crea
        if not nodoDelCaracter:
            # Crear el nuevo trie node
            nivelActual = addTrieNode(nivelActual.children, caracter)
        else:
            nivelActual = nodoDelCaracter

    # Retorna el pointer de la ultima letra
    return nivelActual


def h(key):
    '''
    Explanation:
        Genera un hash en funcion de un entero dado.
    Info:
        This hash function uses 'The multiplication method'
        where (m) is the length of the dictionary and A is φ.
    Params:
        key: The integer from which the hash is to be obtained.
    '''
    return int(m*(key*A % 1))


def addTrieNode(dictionary, key):
    '''
    Explanation:
        Crea un TrieNode y lo inserta en una LList de TrieNodes
    Params:
        dictionary: El pointer del primer TrieNode de la lista
        key: El 
    Return:
        El pointer del nodo creado.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Create the new Trie node
    newNode = TrieNode()
    newNode.children = algo.Array(m, TrieNode())
    newNode.key = key

    # Add the new node to the list of TrieNodes
    newNode.nextTrieNode = dictionary[index]
    dictionary[index] = newNode

    # Return the pointer of the new node
    return newNode
