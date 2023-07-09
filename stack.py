#!/usr/bin/python

# Stack

class Stack:
    """
    Last In First Out(LIFO) Object.
    :push -> Adds elements to the stack
    :pop -> Removes elements from the stack
    :peek -> Shows the last element in the stack.
    """
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            last_elem = self.stack[-1]
            self.stack.remove(last_elem)

    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def __repr__(self):
        return str(self.stack)


