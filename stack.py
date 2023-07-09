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
        self.__stack = []

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if len(self.__stack) > 0:
            self.__stack.pop()

    def peek(self):
        return self.__stack[-1] if len(self.__stack) > 0 else None

    def __repr__(self):
        return str(self.__stack)


