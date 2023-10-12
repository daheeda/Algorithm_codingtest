from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))

res = 0

for i in range(1,n+1):
    for k in list(combinations(arr,i)):
        if sum(k) == s :
            res +=1

print(res)
