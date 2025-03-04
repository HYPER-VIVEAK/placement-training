# #Arrays
# '''
# In array the memory alocation in done by the size of the type of the variable that is for in the memory space is 4 and
# for character it is 1.
# but the memory allocation of the array is static
#
#
# (1)
# vectors
# vectors is a growaable array it multies by 2 that is 4-->--->8-->16--->32--->64
# it can also store same datatype
#
# DSA in pytthon
# List
#
# list in python is not exactly an array it is a vector that behaves like Array
# List is resizable
# List is dynamic sized array which grows and sinks automatically.
# list a Vector which behaves like array but it can store VALUES OF MIXED Data types like int,float, character, string.
# LIst can have  Duplicates
# Lists are ordered, It maintains the order based on how they are ordered.
# List is Mutable
# vectors are powerfull  list is not power full
# list functions are
# sort
# sorted
# add
# remove
# append
#
# Tuple-()
# resizable_dynamic memory allocation
#
# immutable
# duplicates allowed
# ordered
# methods _count Index
#
# <-1->
#
#
#
# binary to ocata decimal
# a = int(input())
# b = a
# i = 1
# pos = 1
# st = ''
#
# while (True):
#     pos = i
#     if 8 ** i  >= a:
#         print("position:",1)
#         break
#     i += 1
# while (pos>=0):
#     for j in range(7, -1, -1):
#         if ((8 ** pos * j) <=b):
#             b = b -( 8 ** pos * j)
#             st = st + str(j)
#             print(j)
#             break
#         elif j == 0:
#             st = st + str(j+1)
#     pos -= 1
# print(int(st))
# set{}
# resizable
# grows and sinks
# Multiple data types
# no duplicates
# unorder,unindexed
# if the same element added again the second element is not accepted
# only add and remove is allowed append is not allowed
#
#
#
# disctionary
#
#
#
#
#
#
#
# #
# # b = int(input())
# # st = ''
# #
# # m = 0
# #
# # while b != 0:
# #
# #     m = b % 8
# #     b = b // 8
# #     st = str(m) + st
# # print(st)
# #
# #hexa to deci
# '''st=input()
# n=len(st)
# n=n-1
# num=0
# dic={
#     'A':10,
#     'B':11,
#     'C':12,
#     'D':13,
#     'E':14,
#     'F':15,
# }
# for i in st:
#  if i in dic:
#     num=num+dic[i]*16**n
#     n-=1
#  else:
#      num = num + int(i) * 16 ** n
#      n -= 1
# print(num)
#
#
# '''
# # n=int(input())
# # m=0
# # for i in range(1,n+1):
# #   for j in range(1,i+1):
# #     print(m,end=" ")
# #     if m==0:
# #       m=1
# #     else:
# #       m=0
# #   print()
# '''l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# for i in range(0,len(l2)):
#   for j in range(0,len(l1)):
#       if l2[i] < l1[j]:
#         l1[j]=l1[j]+l2[i]
#         l2[i]=l1[j]-l2[i]
#         l1[j]=l1[j]-l2[i]
# for i in l2:
#   print(i,end=" ")
# '''
# #Strings in Python
# '''String- Python
#
# A string is a sequence of characters encloded In double quotes.
#
# Python treats anything inside double quotes as string that includes numbers, space, symbols.
#
# Python has no character data type so single character is a string of length 1.
#
# String can be stored using single quotes aand also double quotes. To store multi-line input, triple quotes are allowed.(""" text""")(''' text''')
# String  indexing:+ve index starts from 0 and negative
# index starts from -1 begins from end.'''
#
# # a = input()
# # li = []
# #
# # def cc(c):
# #     if ord(c) > 60:
# #         li.append(chr(ord(c) - 32))
# #     else:
# #         li.append(c)
# #
# # for char in a:
# #     cc(char)
# #
# # for i in li:
# #     print(i, end=' ')
# '''
# Time complexity:
#                 types:
#                     best case (Finding the first elemt in array)
#                     Averase case (Finding the middle element in the array)
#                     Worst case (Findin the last element in array)
# majorly used time complexity in worst case senerios.
#         O(n),0(log n),0(n2)
# """
"""
ponters:
    Ponter can assess its Value, address of the own pinter value,and the value of the pointed value

  """
