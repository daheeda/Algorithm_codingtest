import sys
input = sys.stdin.readline
n = int(input())
w = [int(input()) for _ in range(n)]
w.sort()
max_cur = 0
for k in range(n,0,-1):
    max_try = w[n-k]*k
    if max_cur < max_try :
        max_cur = max_try
print(max_cur)
