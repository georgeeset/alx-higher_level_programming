#!/usr/bin/python3
class Node():
    """ A node class of singly linked list"""

    def __init__(self, data, next_node=None):
        """
        data: contains integer
        next_node: link to next Node connected
        to the current node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self._data = data

        if isinstance(next_node, Node) or (next_node is None):
            self._next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """ Retrieve data """
        return self._data

    @data.setter
    def data(self, value):
        """ Change the value of Data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self._data = value

    @property
    def next_node(self):
        """ Retrieve value of next_node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """ update the value of next_node """
        if isinstance(value, Node) or (value is None):
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """ this vlass defines a singly linked list"""

    def __init__(self,):
        """initialise data"""
        self.head = None

    def __str__(self):
        """ convert the content of singly linked
        list to string
        """
        fullstr = ""
        node = self.head
        while node:
            fullstr += f"{node.data}\n"
            node = node.next_node
        return fullstr[:-1]

    def sorted_insert(self, value):
        """Inserts a node in sorted link list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        point = self.head
        while point.next_node and point.next_node.data < value:
            point = point.next_node
        new_node.next_node = point.next_node
        point.next_node = new_node
