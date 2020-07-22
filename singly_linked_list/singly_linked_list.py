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



# class LinkedList:
#     def __init__(self, head = None):
#         self.head = head


#     def insert(self, value):
#         new_node = Node(value)
#         new_node.set_next(self.head)
#         self.head = new_node

#     def size(self):
#         current = self.head
#         count = 0
#         while current:
#             count += 1
#             current = current.get_next()
#         return count
    
#     def search(self, value):
#         current = self.head
#         found = False
#         while current and found is False:
#             if(current.get_value == value):
#                 found = True
#             else:
#                 current = current.get_next()
#         if current == None:
#             ValueError('Data is not in the list')
#         return current
    
#     def delete(self, value):
#         current = self.head
#         previous = None
#         found = False
#         while current and found is False:
#             if(current.get_value = value):
#                 found = True
#             else:
#                 previous = current
#                 current = current.get_next()
#         if current == None:
#             ValueError('Data is not in the list')
#         if previous == None:
#             self.head = current.get_next()
#         else:
#             previous.set_next(current.get_next())
            


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

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
        current = current.get_next()
        return False