import heapq
import sys
n=int(input())
arr=[]
for i in range(n):
    q = int(sys.stdin.readline())
    heapq.heappush(arr, (-q, q)) # _heapify_max 최대힙제공툴보다빠름
    if q == 0:
        print(heapq.heappop(arr)[1])