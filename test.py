# n = 4
#
# row=(2*n-1)+2
# for i in range(1,n+1):
#     st=(2*(n+1-i)-1)
#     space=(row-st)//2
#
#     for k in range(0,row):
#         if k<space:
#             print(" ",end="")
#         elif k<row-space:
#             print("*",end="")
#
#
#     print()
#

"""
1*2*3*4*16*16*16*16
 5*6*7*9*9*9
  8*9*4*4
   10*1



n = 4
row=2*n
sh=n*(n+1)
fh=sh//2
ef=1

for i in range(0,n):
    st=(2*(n-i))
    space=(row-st)//2
    # print(st)
    # print(row)


    for k in range(0,row):
        if k<space:
            print(" ",end="")
        elif k<row//2:
            print(ef,end='*')
            ef+=1
        elif k<row-space:
            start=sh-((n-i)*2//2)
            if k != row-space-1:
                print(start,end="*")
                start += 1
            else:
                print(start,end="")
                start += 1
    sh=sh-2*(n-i)
    print()
"""

n = 6
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
