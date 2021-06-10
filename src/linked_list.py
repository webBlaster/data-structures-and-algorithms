class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if not self.head:
            self.head = new_element
        while current.next:
            current = current.next
        current.next = new_element