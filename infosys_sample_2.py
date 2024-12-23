def check(a,s,e):
        global n
        for k in range(1,n+1):
            if(a[s]%k==0):
                a[s+1]=k
                if(s+1==e-1):
                    print(a[::-1])
                    global count
                    count = count+1
                else:
                    check(a,s+1,e)
n=int(input())
k=int(input())
a=[0]*k
count = 0
if(k==1):
    count=n
else:
    for i in range(1,n+1):
        a[0]=i
        check(a,0,k)
print(count)