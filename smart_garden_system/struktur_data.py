class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None
    
class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None
    
    def tampil(self):
        for item in self.data:
            print(item)