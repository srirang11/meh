#arr=[0 60 100 40 20 80 90 200 30 15 61 120 84 16 55 190 85 21]
arr=list(map(int,input().split()))
peak=[]
arr.append(arr[len(arr)-1]-1)
if arr[0]>arr[1]:
    peak.append(arr[0])
for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        peak.append(arr[i])
print(peak)
max=peak[0]
for i in range(len(peak)):
    if peak[i]>max:
        max=peak[i]
print(max)