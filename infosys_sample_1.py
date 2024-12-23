n=int(input())
e=int(input())
mon=[]
bon=[]
for i in range(n):
    mon.append(int(input()))
for i in range(n):
    bon.append(int(input()))
for i in range(n):
    for j in range(n-i-1):
        if mon[j] > mon[j+1]:
            mon[j], mon[j+1] = mon[j+1], mon[j]
            bon[j], bon[j+1] = bon[j+1], bon[j]
count=0
for i in range(n):
    if bon[i]>=0 and mon[i]<e:
        count+=1
        e+=bon[i]
for i in range(n):
    for j in range(n-i-1):
        if bon[j] < bon[j+1]:
            mon[j], mon[j+1] = mon[j+1], mon[j]
            bon[j], bon[j+1] = bon[j+1], bon[j]     
for i in range(n):
    if bon[i]<0 and mon[i]<e:
        count+=1
        e+=bon[i] 
print(count)
