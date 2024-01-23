#!/usr/bin/python3
"""defining the Node and Singly Linked List classes."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the list.

        Raises:
            TypeError: If data is not an integer.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gives back the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setting up the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gives back the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting up the next node in the list.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If value is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes a new Linked List instance."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value for the new Node.

        """
        n_node = Node(value)
        if self.head is None or value < self.head.data:
            n_node.next_node = self.head
            self.head = n_node
        else:
            count = self.head
            while count.next_node is not None and count.next_node.data < value:
                count = count.next_node
            n_node.next_node = count.next_node
            count.next_node = n_node

    def __str__(self):
        """Converts the linked list to a string to be printed."""
        result = ""
        count = self.head
        while count is not None:
            result += str(count.data) + "\n"
            count = count.next_node
        return result.strip()
