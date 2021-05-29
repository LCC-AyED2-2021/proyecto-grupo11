## List - sequence ADT implementation

# Define the needed classes
class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None

# Define operations


def add(linkedList, element):
    """
    Explanation: 
        Add an element at the beginning of a LinkedList (sequence ADT).
    Params:
        linkedList: The list on which you want to add the element.
        element: The element to add.
    """
    # Create the new node and store the element.
    newNode = Node()
    newNode.value = element

    # Assign the head node to be the second node
    newNode.nextNode = linkedList.head

    # Assign the new node as the first node
    linkedList.head = newNode


def search(linkedList, element):
    """
    Explanation: 
        Searches for an element in the given list.
    Params:
        linkedList: The list on which you want to perform the search.
        element: The element to search in the given list.
    Return:
        The index where is the element.
        If the element is found multiple times, returns the first index where appears.
        Returns 'None' if the element is not in the list.
    """
    # Define the head of the linked list as the actualNode
    actualNode = linkedList.head

    # Perform the search
    i = -1  # To start with 0
    while actualNode:
        i += 1
        if actualNode.value == element:
            return i
        actualNode = actualNode.nextNode
    return None


def insert(linkedList, element, position):
    """
    Explanation:
        Inserts an element in a given position on a list.
    Params:
        linkedList: The list on which you want to perform the insert.
        element: The element to insert in the given list.
        position: The position of the element to insert.
    Return:
        The index where was inserted the element.
        Returns 'None' if the given position is out of bounds of the list.
    """
    # Case if position is 0
    if position == 0:
        add(linkedList, element)
        return position

    # Go to the node previous to the given position.
    previousNode = getNode(linkedList, position-1)

    # Check if don't exist a previous node (out of bounds).
    if not previousNode:
        return None

    # Create the new node and store the element.
    newNode = Node()
    newNode.value = element

    # Assign new pointers (.nextNode)
    newNode.nextNode = previousNode.nextNode
    previousNode.nextNode = newNode

    # Return the position of the inserted element.
    return position


def delete(linkedList, element):
    """
    Explanation:
        Delete an element on an list.
    Info:
        If exist more than one element, only the first one will be deleted.
    Params:
        linkedList: The list on which you want to perform the delete.
        element: The element to delete in the given list.
    Return:
        The index where was located the deleted element.
        Returns 'None' if the element don't exist on the list.
    """
    # Search and store the position of the element
    position = search(linkedList, element)

    # Case if the element was not found.
    if position == None:
        return None

    # Check if position = 0
    if position == 0:
        # Assign the second node as head
        linkedList.head = linkedList.head.nextNode
    else:
        # Go to the node previous to the position of the element.
        previousNode = getNode(linkedList, position-1)

        # Reassign pointers (.nextNode)
        previousNode.nextNode = previousNode.nextNode.nextNode

    # Return the position where was located the deleted element.
    return position


def length(linkedList):
    """
    Explanation: 
        Count the number of elements of the given list.
    Params:
        linkedList: The list on which you want to perform the count.
    Return:
        The number of elements of the list.
    """
    # Define the head of the linked list as the actualNode
    actualNode = linkedList.head

    # Perform the count
    count = 0
    while actualNode:
        count += 1
        actualNode = actualNode.nextNode
    return count


def access(linkedList, position):
    """
    Explanation: 
        Access to an element in the given position of the list.
    Params:
        linkedList: The list where is located the element to access.
        position: The position of the element in the list.
    Return:
        The value of the element at the given position.
        Returns 'None' if there is no element for that position.
    """
    # Store the node
    actualNode = getNode(linkedList, position)

    # Case if the position is out of bounds.
    if not actualNode:
        return None

    # Return the element
    return actualNode.value


def update(linkedList, element, position):
    """
    Explanation: 
        Update the value of an element in a given position of the list.
    Params:
        linkedList: The list where is located the element to update.
        element: The new value of the element to update in the list.
        position: The position of the element to update in the list.
    Return:
        The position where the update was performed.
        Returns 'None' if there is no element for that position.
    """
    # Store the node
    actualNode = getNode(linkedList, position)

    # Case if the position is out of bounds.
    if not actualNode:
        return None

    # Perform the update
    actualNode.value = element
    return position


def getNode(linkedList, position):
    """
    Explanation:
        Go to the node at the given position.
    Params:
        linkedList: The list where is located the node.
        position: The node's position.
    Return:
        The pointer of the node.
        Returns 'None' if the given position is out of bounds of the list.
    """
    # Case if the position is out of bounds.
    if position > length(linkedList) or position < 0:
        return None

    # Go to the node with the given position.
    actualNode = linkedList.head
    actualPosition = 0
    while (actualPosition != position):
        actualNode = actualNode.nextNode
        actualPosition += 1

    # Return the pointer.
    return actualNode

def moveNode(linkedList, fromPosition, toPosition):
    """
    Explanation:
        Move a node from a given position to an other.
    Params:
        linkedList: The list where is located the node.
        fromPosition: The node's actual position.
        toPosition: The position where the node will be placed.
    Return:
        The position where the node was moved
        Returns 'None' if the given position is out of bounds of the list.
    """
    # Case same from and to positions
    if fromPosition == toPosition:
        return toPosition

    # Case out of bounds
    lengthOfLList = length(linkedList)
    if (fromPosition < 0 or toPosition < 0
        or fromPosition >= lengthOfLList or toPosition >= lengthOfLList):
        return None

    # From Position Node Part
    previousFromNode = getNode(linkedList, fromPosition-1)
    fromNode = None

    if not previousFromNode:  # Head case
        fromNode = getNode(linkedList, fromPosition)
        linkedList.head = fromNode.nextNode
    else:
        fromNode = previousFromNode.nextNode
        previousFromNode.nextNode = fromNode.nextNode

    # To Position Node Part
    previousToNode = getNode(linkedList, toPosition-1)

    if not previousToNode:  # Head case
        toNode = getNode(linkedList, toPosition)
        fromNode.nextNode = toNode
        linkedList.head = fromNode
    else:
        toNode = previousToNode.nextNode
        fromNode.nextNode = toNode
        previousToNode.nextNode = fromNode

    # Return the position of the movedNode
    return toPosition

def swapNodes(linkedList, firstNodePosition, secondNodePosition):
    """
    Explanation:
        Swap the position of two nodes of a Linked List.
    Params:
        linkedList: The list where is located the node.
        firstNodePosition: The position of the first node to swap.
        secondNodePosition: The position of the second node to swap.
    Return:
        '1' if the swap was successful.
        Retruns 'None' if the list is empty, or given positions are out of bounds.
    """
    # Case empty list
    if not linkedList.head:
        return None

    # Case same from and to positions
    if firstNodePosition == secondNodePosition:
        return 1

    # Case out of bounds
    lengthOfLList = length(linkedList)
    if (firstNodePosition < 0 or secondNodePosition < 0 or firstNodePosition >= lengthOfLList
        or secondNodePosition >= lengthOfLList):
        return None

    prevFirstNode = getNode(linkedList, firstNodePosition-1)
    prevSecondNode = getNode(linkedList, secondNodePosition-1)
    if not prevFirstNode:
        firstNode = linkedList.head
        secondNode = prevSecondNode.nextNode
    else:
        firstNode = prevFirstNode.nextNode
        if not prevSecondNode:
            secondNode = linkedList.head
        else:
            secondNode = prevSecondNode.nextNode

    if firstNode and secondNode:
        # Swap prevNodes or head
        if prevFirstNode:
            prevFirstNode.nextNode = secondNode
        else:
            linkedList.head = secondNode

        if prevSecondNode:
            prevSecondNode.nextNode = firstNode
        else:
            linkedList.head = firstNode

        # Swap nextNodes
        tempNode = firstNode.nextNode
        firstNode.nextNode = secondNode.nextNode
        secondNode.nextNode = tempNode
    return 1