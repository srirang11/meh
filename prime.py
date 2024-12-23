l=int(input())
u=int(input())
for i in range(l+1,u):
    f=-1
    if i<2:
        continue
    elif i==2:
        print(i)
    else:
        for j in range(2,i):
            if i%j==0:
                f+=1
        if f==-1:
            print(i)