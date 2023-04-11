import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
arr = deque(range(1, n + 1))
index = k-1
res="<"
cnt=0
for i in range(0,n):
    if index >= len(arr) :
        index = (index) % len(arr)
        res += str(arr[index])+", "
        arr.remove(arr[index])
    else :
        res += str(arr[index])+", "
        arr.remove(arr[index])
    index += k -1

print(res[:-2]+">")
