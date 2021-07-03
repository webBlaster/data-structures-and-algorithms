class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head == None:
            self.head = new_element
            return
        while current.next:
            current = current.next
        current.next = new_element

    def print_value(self):
        if self.head != None:
            print(self.head.next)


first_element = Element(2)
second_element = Element(12)
third_element = Element(4)

linked_list = LinkedList()
linked_list.print_value()
linked_list.append(first_element)
linked_list.print_value()
linked_list.append(second_element)
linked_list.print_value()
linked_list.append(third_element)
linked_list.print_value()
