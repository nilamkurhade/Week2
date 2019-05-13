class Stack:
    def __init__(self):        # Constructor of class and creating empty stack
        self.items = []

    def isEmpty(self):         # Checking Stack is empty or not
        return self.items == []

    def push(self, item):       # pushing elements into stack
        self.items.append(item)

    def pop(self):      # Removing elements from stack
        return self.items.pop()

    def peek(self):     # Getting highest index of stack
        return self.items[len(self.items) - 1]

    def size(self):     # Checking the size of the stack
        return len(self.items)
