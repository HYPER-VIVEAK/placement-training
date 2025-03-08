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
#Start your Coding Race
# Start your coding Race
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sll:
    head=None

    def __init__(self):
        self.head == None

    def inend(self, data):
            nod = Node(data)
            if self.head == None:
                self.head = nod
                return
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = nod

            return
    def inatposition(self,pos,data):
        nod = Node(data)
        len=0
        temp = self.head
        while temp:
            temp = temp.next
            len+=1


        if self.head == None:
            print("Empty list")


        else:
            prev=self.head
            nex=self.head.next
            for i in range(1,len+1):
                 if  pos==0:
                   nod.next =self.head
                   self.head = nod
                   return
                 elif pos==i:
                     nod.next=nex
                     prev.next=nod
                     return

                 prev=prev.next
                 nex=nex.next
    def delb(self):
        temp=self.head
        self.head=temp.next
        return
    def dele(self):
        temp=self.head
        while temp.next.next!=None:
          temp=temp.next
        temp.next=None
    def delatpos(self,pos):
        len = 0
        temp = self.head
        while temp:
            temp = temp.next
            len += 1

        if self.head == None:
            print("Empty list")


        else:
            temp = self.head
            for i in range(1, len + 1):
                if pos == 0:
                    self.head=temp.next
                elif pos == i:
                    temp.next=temp.next.next
                    return
                temp=temp.next


    def disp(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

s=Sll()
s.inend(50)
s.inend(9)
s.inend(78)
s.inend(82)
s.disp()

s.inatposition(4,34)
s.disp()
s.delatpos(2)
s.disp()



