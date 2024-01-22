class Stack:
    def __init__(self):
        self.items = []
    
    def is_stack_empty(self):
        return len(self.items) == 0

    def add_item(self,item):
        self.items.append(item)

    def pop_item(self):
        if not self.is_stack_empty():
            return self.items.pop()
        print("Info: stack is empty")

    def item_at_the_top(self):
        if not self.is_stack_empty():
            return self.items[-1]
        print("Info: stack is empty")

    def stack_size(self):
        return len(self.items)
    

event_stack = Stack()
tasks = ["Wake up","Brush teeth", "Take a dump", "Work out", "Take bath", "Work a bit", "Sort out food"]

for task in tasks:
    event_stack.add_item(task)
    print("Resolving task:")
    print(event_stack.pop_item())

