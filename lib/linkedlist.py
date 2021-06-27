# List - sequence ADT implementation

# Define the needed classes
class LinkedList:
    head = None


class Node:
    value = None
    key = None
    nextNode = None

# Define operations


def add(L, element, cont):
    NodeA = L.head  # Definimos NodeA como LinkedList
    if NodeA != None:  # Si este no es None:
        NodeB = Node()  # Se crea otro Node
        NodeB.value = element  # Le damos valor al NodeB
        NodeB.key = cont
        NodeB.nextNode = NodeA  # Igualamos
        L.head = NodeB
    else:  # Si la primer lista no es None:
        NodeB = Node()  # Se crea otro Node
        NodeB.value = element  # Le damos valor al NodeB
        NodeB.key = cont
        L.head = NodeB
