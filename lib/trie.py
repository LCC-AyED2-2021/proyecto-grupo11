########
# Esta implementación esta modificada para trabajar con TrieNodes especiales,
# que poseen un atributo (docsWhereApears) que corresponde a una linked list, con los nombres 
# de los documentos donde la palabra aparece, y cuantas veces aparece.
########

# Trie data structure implementation
import lib.linkedlist as LL
import lib.algo1 as algo
import lib.mydictionary as D
from lib.latinHash import latinHash as LHash

# Define classes

class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    docsWhereApears = None

# Define functions


def insert(trie, element):
    '''
    Explicación:
        Inserta un elemento en el Trie dado.
    Parametros:
        trie: El Trie en donde se insertará el elemento.
        element: La palabra a insertar.
    Return:
        El puntero de la ultima letra de la palabra insertada.
    '''
    # Caso Trie no inicializado
    if not trie.root:
        # Se inicializa, children es una hash table
        trie.root = TrieNode()
        trie.root.children = algo.Array(11, LL.LinkedList())

    # Convertir el elemento dado a text usando algo1
    text = algo.String(element)

    # Comparar cada nivel del trie con el indice actual de text
    currentLevel = trie.root

    for i in range(0, len(text)):
        # Buscar el caracter en el nivel actual
        caracter = LHash(text[i])
        hashCaracter = D.h(caracter)
        nodoDelCaracter = D.getNodeByKey(currentLevel.children[hashCaracter], caracter)

        if not nodoDelCaracter:
            # Create the new trie node
            currentLevel = (D.insert(currentLevel.children, caracter, caracter, currentLevel)).value
            
        else:
            currentLevel = nodoDelCaracter.value

    # Retorna el pointer de la ultima letra
    return currentLevel
