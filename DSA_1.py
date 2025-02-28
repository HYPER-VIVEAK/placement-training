#Arrays
'''
In array the memory alocation in done by the size of the type of the variable that is for in the memory space is 4 and
for character it is 1.
but the memory allocation of the array is static


(1)
vectors
vectors is a growaable array it multies by 2 that is 4-->--->8-->16--->32--->64
it can also store same datatype

DSA in pytthon
List

list in python is not exactly an array it is a vector that behaves like Array
List is resizable
List is dynamic sized array which grows and sinks automatically.
list a Vector which behaves like array but it can store VALUES OF MIXED Data types like int,float, character, string.
LIst can have  Duplicates
Lists are ordered, It maintains the order based on how they are ordered.
List is Mutable
vectors are powerfull  list is not power full
list functions are
sort
sorted
add
remove
append

Tuple-()
resizable_dynamic memory allocation

immutable
duplicates allowed
ordered
methods _count Index

<-1->



binary to ocata decimal
a = int(input())
b = a
i = 1
pos = 1
st = ''

while (True):
    pos = i
    if 8 ** i  >= a:
        print("position:",1)
        break
    i += 1
while (pos>=0):
    for j in range(7, -1, -1):
        if ((8 ** pos * j) <=b):
            b = b -( 8 ** pos * j)
            st = st + str(j)
            print(j)
            break
        elif j == 0:
            st = st + str(j+1)
    pos -= 1
print(int(st))

'''
