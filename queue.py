from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_queue_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_queue_empty():
            return self.queue.popleft()
        print("Info: queue is empty")

    def front_of_queue(self):
        if not self.is_queue_empty():
            return self.queue[0]
    
    def queue_size(self):
        return len(self.queue)

        