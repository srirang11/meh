# # I decided to go to a temple and give offerings to god. i decided to give lemons to goddess. There are 3 goddesses in that temple. Only 7 lemons has to be offered to each goddess.
# # Take no of lemos in hand from the user as input. 
# print("Number of lemons: ")
# n=int(input())
# def lemon(n):
#     c=n//7
#     if n<=0:
#         c="a"
#         n=0    
#     match(c):
#         case "a":
#             print("God1:want",7)
#             print("God2:want",7)
#             print("God3:want",7)
#         case 0:
#             print("God1:Can offer",n,"want",7-n)
#             print("God2:want",7)
#             print("God3:want",7)
#         case 1:
#             print("God1:Offered",7)
#             print("God2:Can offer",n-7,"want",14-n)
#             print("God3:want",7)
#         case 2:
#             print("God1:Offered",7)
#             print("God2:Offered",7)
#             print("God3:Can offer",n-14,"want",21-n)
#         case _:
#             print("God1:Offered",7)
#             print("God2:Offered",7)
#             print("God3:Offered",7)
#     if n>21:
#         print("Surplus:",n-21)
#     elif n==21:
#         print()
#     else:
#         print("Insufficient:",21-n)
#     print("God Bless You.")
# lemon(n)
# s=input()
# k=int(input())
# n=len(s)
# ss=""
# t=0
# for i in range(n):
#     if t==k:
#         break
#     if s[i] not in ss:
#         ss=ss+s[i]
#     if (i+1)%(n//k)==0:
#         print(ss)
#         ss=''
#         t+=1

i=()
