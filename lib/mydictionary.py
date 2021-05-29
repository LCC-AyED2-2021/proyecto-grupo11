from lib import algo1, linkedlist as LL, trie as T

# Def dictionaryNode (analog to linkedlist's node)

class dictionaryNode:
    key = None
    value = None
    nextNode = None


# Define global constants and dictionaries
m = 11  # Length of the dictionary
A = ((5**.5 - 1)/2) # Golden ratio φ

# Define functions

def h(key):
    '''
    Explanation:
        Generates a hash for a given integer.
    Info:
        This hash function uses 'The multiplication method'
        where (m) is the length of the dictionary and A is φ.
    Params:
        key: The integer from which the hash is to be obtained.
    '''
    return int(m*(key*A % 1))


def insert(dictionary, key, value, parent):
    '''
    Explanation:
        Inserts a value in a dictionary (using hash tables).
    Info:
        If the key to insert is already in the table, the old value will be overwritten.
    Params:
        dictionary: The dictionary on which you want to perform the insert.
        key: The key of the value to be inserted.
        value: The key of the trieNode to be created. !!
        parent: The parent of the new node
    Return:
        The pointer of the created node.
    '''
    # Obtain the hash of the given key
    index = h(key)

    # Define a variable to store pointer
    pointer = None

    # Create the new Trie node
    newNode = T.TrieNode()
    newNode.children = algo1.Array(11, LL.LinkedList())
    newNode.key = value
    newNode.parent = parent


    # Create the LinkedList if the index is empty
    if not dictionary[index]:
        dictionary[index] = LL.LinkedList()

    # Add the new node to the list
    pointer = add(dictionary[index], key, newNode)

    # Return the pointer of the new node
    return pointer


def add(linkedList, key, value):
    '''
    Explanation: 
        Add an element at the beginning of a Linked List (sequence ADT).
    Info:
        This add function differs from the implementation of Linked list
        because this function creates a dictionaryNode (which has as an addition a key value).
    Params:
        linkedList: The list on which you want to add the element.
        key: The key of the inserted node.
        value: The value to add.
    Return:
        The pointer of the created node
    '''
    # Create the new node and store value and key.
    newNode = dictionaryNode()
    newNode.key = key
    newNode.value = value

    # Assign the head node to be the second node
    newNode.nextNode = linkedList.head

    # Assign the new node as the first node
    linkedList.head = newNode

    # Return the pointer of the created node
    return newNode

def getNodeByKey(linkedList, key):
    '''
    Explanation: 
        Searches for a key in a given linkedlist of dictionaryNodes.
    Params:
        linkedList: The list on which you want to perform the operation.
        key: The key to search in the given list.
    Return:
        The pointer of the node.
        Returns 'None' if there is not a node with the given key.
    '''
    # Define a result variable to store the pointer if exists.
    pointer = None

    # Search until a key coincidence
    if linkedList:
        actualNode = linkedList.head
        while actualNode:
            if actualNode.key is key:
                pointer = actualNode  # Store the pointer
                break
            actualNode = actualNode.nextNode

    # Return the result value
    return pointer
