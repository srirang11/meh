# import calcnew
# print(calcnew.mul(23,10))
n=int(input())
a=[]
r=[]
a1=[]
for i in range(n):
    r.append(input())
    r.append(float(input()))
    a.append(r)
    r=[]
s=[a[i][1] for i in range(n)]
s=set(s)
s1=sorted(s)
for i in range(n):
    if a[i][1]==s1[1]:
        a1.append(a[i][0])
a1=sorted(a1)
for i in a1:
    print(i)