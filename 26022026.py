#patters
# # # # # # *
# # # # # * *
# # # # * * *
# # # * * * *
# # * * * * *
# * * * * * *
# To print

# to find starting and ending of the lopps
# here i ranges from 0 to n
#      j ranges from i to n
#      k ranges from 0 to i+1:

# and need to trace the loops to follow exact working of the loop

n=6
for i in range(0,n):#outer loop next line loop
    for j in range(i,n):#prints Space
        print(" ",end="")
    for k in range(0,i+1):#prints *
        print("*",end=" ")
    print(" ")
print("1--------------------------------------------------------------------------------------------------")

n2=6
for i in range(0,n2):
    for j in range(0,i+1):
        print("  ",end="")
    for k in range(i,n):
        print("*",end=" ")
    print("")
print("2------------------------------------------------------------------------------------------------------")
n3=6
for i in range(0,n2):
    for j in range(0,i+1):
        print(j+1,end=" ")
    for k in range(i,n):
        print(" ",end="")
    print("")
print("3------------------------------------------------------------------------------------------------------")
# n=int(input("Enter"))
n=6
t1=n+1
for i in range(0,t1):#outer loop next line loop
    for j in range(i,t1-1):#prints Space
        print(" ",end="")
    for k in range(0,2*i-1):#prints *
        print("*",end="")
    print("")
t2=t1-2
for i in range(0,t2):#outer loop next line loop
    for j in range(0,i+1):#prints Space
        print(" ",end="")
    for k in range(0,2*(t2-i)-1):#prints *
        print("*",end="")
    print("")

print("4--------------------------------------------------------------------------------------------------")
# n=int(input("Enter"))
n=6
t1=n+1
t2=t1-1
for i in range(0,t2):#outer loop next line loop
    for j in range(1,i+1):#prints Space
        print(" ",end="")
    for k in range(0,2*(t2-i)-1):#prints *
        print("*",end="")
    print("")
for i in range(0,t1):#outer loop next line loop
    for j in range(i,t1-1):#prints Space
        print(" ",end="")
    for k in range(0,2*i-1):#prints *
        print("*",end="")
    print("")



print("5--------------------------------------------------------------------------------------------------")
