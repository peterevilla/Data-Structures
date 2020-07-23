"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Using regular List
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:              
#             self.storage.pop()
#             self.size -= 1

# stack1 = Stack()
# stack1.push(5)
# print(stack1.storage)


# using Linked List

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 1:
            self.storage.remove_head()
            self.size -= 1
        elif self.size > 1:              
            self.storage.remove_tail()
            self.size -= 1


stack2 = Stack()

stack2.push(5)
stack2.push(6)
stack2.push(8)
stack2.pop()

node = stack2.storage.head
while node:
    print (node.value)
    node = node.get_next()

