a=list(map(int,input().split()))
print(a)
for j in range(len(a)//2):
    a[j],a[len(a)-1-j]=a[len(a)-1-j],a[j]
print(a)