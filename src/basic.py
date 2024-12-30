class Stack:
    def __init__(self):
        self.items = list()
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


class Queue:
    def __init__(self) -> None:
        self._data = list()

    def isEmpty(self):
        return len(self._data) == 0
    
    def enqueue(self, val):
        self._data.append(val)
        # self._data.insert(0, val)

    def dequeue(self):
        return self._data.pop(0)
        # return self._data.pop()

    def size(self):
        return len(self._data)