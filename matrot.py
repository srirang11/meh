r=int(input("Enter no of rows:"))
c=int(input("Enter no of columns:"))
n=max(r,c)
a=[[[0] for i in range(n)]for j in range(n)]
row=[]
for i in range(r):
    for j in range(c):
        a[i][j]=int(input(f"Enter a[{i}][{j}]:"))

print("Matrix:\n")
for i in range(r):
    print(a[i][:c])

for i in range(n):
    for j in range(i,n):
        a[i][j],a[j][i]=a[j][i],a[i][j]

print("Rotated matrix:\n")
for i in range(c):
    t=a[i][:r]
    print(t[::-1])