#!/bin/env python3

# This is an implementation of a Stack in python

class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self,item):
        return self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items)-1]



