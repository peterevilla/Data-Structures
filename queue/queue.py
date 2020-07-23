"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
    
    def remove_tail(self):
        if not self.tail:
            return None
        

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
        current = current.get_next()
        return False


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        pass

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        self.storage.remove_head()

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         pass

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         self.storage.pop()

#QUEUE USING A REGLAR LIST
queue1 = Queue()

nextQueue = input("enter next number to queue, press r to remove next in queue, press q to quit\n")

while not nextQueue == 'q':

    if nextQueue != 'r':
        queue1.enqueue(int(nextQueue))
        print(queue1.storage)
        
    elif nextQueue == 'r':
        queue1.dequeue()
        print(queue1.storage)
    else:
        print('invalid character')

    nextQueue = input("enter next number to queue, press r to remove next in queue, press q to quit\n")

print('\n')
node = queue1.storage.head
while node:
    print (node.value)
    node = node.get_next()