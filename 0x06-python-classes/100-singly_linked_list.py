class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node
