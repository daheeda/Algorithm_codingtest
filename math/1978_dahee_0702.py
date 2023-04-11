N = int(input())
val=input().split(" ")
arr=[]

for i in range(0,N):
    arr.append(int(val[i]))

def is_true(num):
    if num == 1 :
        return 0
    for i in range(2,num+1):
        if num != i :
            if num%i == 0 :
                return 0

for i in range(0,len(arr)):
    arr[i]=is_true(arr[i])
    
print(N-arr.count(0))
