class Node:
    def __init__(self, data):
        """Store the data, and set next to None"""
        self.data = data
        self.next = None

    def __str__(self):
        """Return a string representation of the data"""
        return str(self.data)


class Storage:
    def __init__(self):
        """Creates an empty Storage class. Sets head to None."""
        self.head = None

    def push(self, data):
        """Create a Node to hold the data, then put it at the head of the list."""
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        """Remove the head Node and return its data."""
        n = self.head
        if n == None:
            return
        else:
            self.head = n.next
            return n.data

    def peek(self):
        """Return the data from the head Node, without removing it."""
        return self.head.data

    def isempty(self):
        """Return True if the list is empty, otherwise False"""
        if self.head == None:
            return True
        return False
