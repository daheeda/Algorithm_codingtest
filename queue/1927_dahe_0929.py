import heapq
import sys
n = int(input())
arr=[]

for i in range(n):
    value = int(sys.stdin.readline()) # 입력받는숫자큰경우 sys 사용
    heapq.heappush(arr, value)
    if value == 0 :
        try:
            heapq.heappop(arr)
            print(heapq.heappop(arr))
        except :
            print(0)