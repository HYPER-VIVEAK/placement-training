"""class Books:
    title=''
    author=''
    year=0
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
b1=Books("c++","Bala Guru sami",2005)
print(b1.title)
print(b1.author)
print(b1.year)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        # If the node to be deleted is the head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
    def printlsit(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
            print(temp.data)

a=LinkedList();
a.insert_at_end(29)
a.insert_at_end(30)
a.insert_at_end(56)
a.insert_at_end(2)
a.insert_at_end(9)
a.insert_at_end(88)
a.insert_at_end(7)

a.printlsit()