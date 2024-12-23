n=int(input("Enter no of rows and columns:"))
a=[[[0] for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=int(input(f"Enter a[{i}][{j}]:"))
print("Matrix:")
for i in range(n):
    print(a[i])
print("Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if j==i:
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("\n",end="")
print()
print("Lower Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if j>i:
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("\n",end="")
print()
print("Upper Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if i>j:
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("\n",end="")
print()
print("Non Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if i!=j:
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("\n",end="")
print()
