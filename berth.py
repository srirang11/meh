name=input()
bno=int(input())
d={1:"Lower",2:"Middle",3:"Upper",4:"Lower",5:"Middle",6:"Upper",7:"Side Lower",0:"Side Upper"}
print(d[bno%8])