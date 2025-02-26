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
n=int(input("Enter"))
n=n+1
for i in range(0,n):#outer loop next line loop
    for j in range(i,n-1):#prints Space
        print(" ",end="")
    for k in range(0,2*i-1):#prints *
        print("*",end="")
    print("")
n=n-2
for i in range(0,n):#outer loop next line loop
    for j in range(0,i+1):#prints Space
        print(" ",end="")
    for k in range(0,2*(n-i)-1):#prints *
        print("*",end="")
    print("")

print("4--------------------------------------------------------------------------------------------------")
