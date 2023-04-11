a,b = input().split()
a=int(a)
b=int(b)

arr=[i for i in range(0,b+1)]
arr[1]=0

for i in range(2,b):
    for j in range(2,int((len(arr)-1)//i)+1):
        arr[j*i]=0

for i in range(a,len(arr)):
    if arr[i] !=0:
        print(arr[i])
