class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return
        self.head = new_node

    def prepend(self, new_node):
        if self.head:
            current = self.head
            self.head = new_node
            self.head.next = current
            return
        self.head = new_node

    def delete_node(self, key):
        return

    def print_all(self):
        if self.head:
            current = self.head
            while current.next:
                print(current.data)
                current = current.next
            return
        print("Empty")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

l_list = LinkedList()

l_list.append(node1)

l_list.append(node2)

l_list.append(node3)

l_list.append(node4)

l_list.prepend(node5)

l_list.print_all()
