class Node:

    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.set_next(node)
            self.head = node

    def remove_from_head(self):
        val = None
        if self.head == None:
            val = None
        elif self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
        return val
