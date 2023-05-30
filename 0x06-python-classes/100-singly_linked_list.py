#!/usr/bin/python3
"""
creating linked list class
"""


class Node:
    """
    class for linked list node
    """

    def __init__(self, data, next_node=None):
        """"initiating linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setting the data for the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """return next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setting next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """"linked list class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """String representation of singly linked list needed to print"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """sort the link list by order"""
        new = Node(value)
        if self.__head is None:
            self.__head = new

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
