# #patters
# # # # # # # *
# # # # # # * *
# # # # # * * *
# # # # * * * *
# # # * * * * *
# # * * * * * *
# # To print
#
# # to find starting and ending of the lopps
# # here i ranges from 0 to n
# #      j ranges from i to n
# #      k ranges from 0 to i+1:
#
# # and need to trace the loops to follow exact working of the loop
#
# n=6
# for i in range(0,n):#outer loop next line loop
#     for j in range(i,n):#prints Space
#         print(" ",end="")
#     for k in range(0,i+1):#prints *
#         print("*",end=" ")
#     print(" ")
# print("1--------------------------------------------------------------------------------------------------")
#
# n2=6
# for i in range(0,n2):
#     for j in range(0,i+1):
#         print("  ",end="")
#     for k in range(i,n):
#         print("*",end=" ")
#     print("")
# print("2------------------------------------------------------------------------------------------------------")
# n3=6
# for i in range(0,n2):
#     for j in range(0,i+1):
#         print(j+1,end=" ")
#     for k in range(i,n):
#         print(" ",end="")
#     print("")
# print("3------------------------------------------------------------------------------------------------------")
# # n=int(input("Enter"))
# n=6
# t1=n+1
# for i in range(0,t1):#outer loop next line loop
#     for j in range(i,t1-1):#prints Space
#         print(" ",end="")
#     for k in range(0,2*i-1):#prints *
#         print("*",end="")
#     print("")
# t2=t1-2
# for i in range(0,t2):#outer loop next line loop
#     for j in range(0,i+1):#prints Space
#         print(" ",end="")
#     for k in range(0,2*(t2-i)-1):#prints *
#         print("*",end="")
#     print("")
#
# print("4--------------------------------------------------------------------------------------------------")
# # n=int(input("Enter"))
# n=6
# t1=n+1
# t2=t1-1
# for i in range(0,t2):#outer loop next line loop
#     for j in range(1,i+1):#prints Space
#         print(" ",end="")
#     for k in range(0,2*(t2-i)-1):#prints *
#         print("*",end="")
#     print("")
# for i in range(0,t1):#outer loop next line loop
#     for j in range(i,t1-1):#prints Space
#         print(" ",end="")
#     for k in range(0,2*i-1):#prints *
#         print("*",end="")
#     print("")
#
#
#
# print("5--------------------------------------------------------------------------------------------------")
# a =5
# for i in range(0,a):
#     for j in range(0,a):
#         if i==0 or   i==a-1 or j==0 or j==a-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")
# print("6==============================================================================================")
# a=float(input())
# a=round(a,2)
# print(a)
#
#


"""n = 6
row=2*n
sh=n*(n+1)
fh=sh//2
ef=1
start=0

for i in range(0,n):
    st=(2*(n-i))
    space=(row-st)//2
    start = sh - (((n - i) * 2 // 2)-1)
    # print(st)
    # print(row)


    for k in range(0,row):
        # if k==0 and i!=0:
        #     print("",end="")
        if k<space:
            print(2*" ",end="")
        elif k<row//2:
            print(ef,end='*')
            ef+=1
        elif k<row-space:

            if k != row-space-1:
                print(start,end="*")
                start += 1
            else:
                print(start,end="")
                start += 1
    sh -=st//2

    print()


    output
    1 * 2 * 3 * 4 * 5 * 6 * 37 * 38 * 39 * 40 * 41 * 42
    7 * 8 * 9 * 10 * 11 * 32 * 33 * 34 * 35 * 36
    12 * 13 * 14 * 15 * 28 * 29 * 30 * 31
    16 * 17 * 18 * 25 * 26 * 27
    19 * 20 * 23 * 24
    21 * 22

"""


