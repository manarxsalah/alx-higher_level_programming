#!/usr/bin/python3
"""Define classes for singly-listed list"""


class Node:
    """Represents a node in singly-listed list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node
        Args:
            data (int): the data of the new node
            nex_node (Node): the next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value

class SinglyLinkedList:
    """Represents a singly-linked list"""

    def __init__(self):
        """Initialize a new SingluLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList
        the node is inserted into the list in the
        correct ordered position
        Args:
            Value (Node): the new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
