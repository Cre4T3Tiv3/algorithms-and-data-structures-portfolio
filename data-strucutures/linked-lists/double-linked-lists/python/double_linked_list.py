class Node:
    """
    A class to represent a node in a double linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Node): Reference to the next node in the list.
        prev (Node): Reference to the previous node in the list.
    """

    def __init__(self, data=None):
        self.data = data  # Initialize the node's data.
        self.next = None  # Initially, the next reference is None.
        self.prev = None  # Initially, the previous reference is None.


class DoubleLinkedList:
    """
    A class to represent a double linked list.

    Attributes:
        head (Node): The head node of the list.

    Methods:
        append(data): Appends a new node with the given data to the list.
        display(): Returns a list of all elements in the linked list.
        is_empty(): Checks if the linked list is empty.
        size(): Returns the size of the linked list.
    """

    def __init__(self):
        self.head = None  # Initialize the head of the list.

    def append(self, data):
        """
        Append a node with the given data to the end of the list.

        Parameters:
            data (Any): The data to be stored in the new node.
        """
        if not self.head:
            # If the list is empty, create a new node and set it as the head.
            self.head = Node(data)
        else:
            # If the list is not empty, find the last node and append the new node.
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def display(self):
        """
        Return a list containing all elements of the linked list.

        Returns:
            List[Any]: A list of all the data elements in the linked list.
        """
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return elements

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def size(self):
        """
        Return the size (number of elements) of the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
