"""# Start your coding Race
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    head = 0

    def __init__(self):
        self.head == None

    def inend(self, data):
        temp = self.head
        while temp.next :
            temp = temp.next
        nod = Node(data)
        temp.next=nod

        return

    def inbegin(self, data):
        temp = self.head
        nod = Node(data)
        nod.next = self.head
        self.head = nod
        return

    def disp(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

l1=[]
lis = Sll()
for i in range(0,n):
    l1.append(int(input()))
element=int (input())

for i in l1[::-1]:
    lis.inbegin(i)
lis.inbegin(50)
lis.inbegin(55)
lis.inbegin(6)
lis.inbegin(88)
lis.inbegin(99)

lis.inend(90)
lis.disp()



"""


# Start your Coding Race
# Start your coding Race
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    head = None

    def __init__(self):
        self.head == None

        return

    def disp(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


s = Sll()
s.inend(50)
s.inend(9)
s.inend(78)
s.inend(82)
s.disp()