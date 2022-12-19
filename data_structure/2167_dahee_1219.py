import sys
input = sys.stdin.readline
from itertools import accumulate
n,m = map(int,input().split())

arr = []
for _ in range(n) :
    i = list(map(int,input().split()))
    i = list(accumulate(i))
    i.insert(0,0)
    arr.append(i)

k = int(input())
arr2=[]
for _ in range(k) :
    s = list(map(int,input().split()))
    arr2.append(s)

for index in range(k):
    i = arr2[index][0]-1
    j = arr2[index][1]
    x = arr2[index][2]-1
    y = arr2[index][3]
    res = 0
    for tt in range(i,x+1):
        res += (arr[tt][y]-arr[tt][j-1])
    print(res)
