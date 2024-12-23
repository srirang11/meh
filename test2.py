# climbing ladder

# r=[100,90,90,80]
# p=[70,80,105]
# r=r[:200000]
# p=p[:200000]
# d=[]
# res=[]
# l=0
# for i in r:
#     if i not in d:
#         d.append(i)
#         l+=1
# print(d)
# for i in p:
#     f=1
#     for j in range(l):
#         if i>=d[j] and f==1:
#             res.append(j+1)
#             f=0
#     if f:
#         res.append(l+1)
# print(res)

# import math
# a=int(input())
# b=int(input())
# print(math.degrees(math.atan(a/b)))
# # if t-int(t)>=0.5:
# #     t=int(t+1)
# # else:
# #     t=int(t)
# # print(f"{t}°") 

# import itertools
# s=input()
# r=""
# for k,g in itertools.groupby(s,lambda x:x[0]):
#     l=list(g)
#     r+=f"({len(l)},{k})"
# print(r)

# import itertools
# n=int(input())
# let="".join(input().split())
# k=int(input())
# c=0
# comb=list(itertools.combinations(let,k))
# for i in comb:
#     if "a" in i:
#         c+=1
# print(c/len(comb))


# import re
# s=input()
# k=input()
# l=None
# x=re.search(k,s)
# if not x:
#     print("(-1, -1)")
# while x:
#     if l==x.start():
#         s=s.replace(s[x.start()],"+",1)
#     elif x:
#         print(f"({x.start()}, {x.end()-1})")
#         s=s.replace(s[x.start()],"+",1)
#         l=x.start()
#     x=re.search(k,s)

# import re
# n=int(input())
# s=""
# for i in range(n):
#     s+=input()+"\n"
# s=re.sub("\s&{2}\s"," and ",s)
# s=re.sub("\s\|\|\s"," or ",s)
# s=re.sub("\s&{2}\s"," and ",s)
# s=re.sub("\s\|\|\s"," or ",s)
# print(s)

# import re
# n=int(input())
# for i in range(n):
#     s=input()
#     j=None
#     c=0
#     for i in s:
#         print(i,j,c)
#         if i=="-":
#             continue
#         if j==i:
#             c+=1
#         else:
#             c=0
#         j=i
#         if c==3:
#             break
#     x=re.match("^[456]\d{15}$|^[456]\d{3}-\d{4}-\d{4}-\d{4}$",s)
#     if x and c!=3:
#         print("Valid")
#     else:
#         print("Invalid")


# import itertools
# n,m=map(int,input().split())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
#     a[i].pop(0)
# max=-1
# for i in itertools.product(*a):
#     s=0
#     for j in i:
#         s+=j*j
#     s=s%m
#     if s>max:
#         max=s
# print(max)    

# regex_integer_in_range = r"[1-9]\d{5}"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"(\d)(.\d\1)"	# Do not delete 'r'.


# import re
# P = input()
# print(re.findall(regex_alternating_repetitive_digit_pair, P))
# print (bool(re.match(regex_integer_in_range, P)) 
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
s=""
for i in range(m):
    for j in range(n):
        s+=matrix[j][i]
r=re.findall("(?<=\w)[^\w]+(?=\w)",s)

s=re.sub("(?<=\w)[^\w]+(?=\w)"," ",s)
print(s)