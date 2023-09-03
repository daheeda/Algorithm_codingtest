n = int(input())

arr = [0]*(n+1)

for i in range(1,n+1):

    k1 = i%10
    k2 = int(i*0.1)%10
    k3 = int(i*0.01)%10
    
    if i < 100:
        arr[i] = 1
    else :
        if k1-k2 == k2-k3 :
            arr[i] = 1
if n == 1000 : arr[1000] = 0
print(sum(arr))
