#값에 대한 잦은 수정이 있는경우, 
#계속 정렬을 해야하는 경우는 heap을 사용하는게 효과적입니다.
import heapq
n = int(input())
arr=[]

for i in range(n) :
    heapq.heappush(arr, int(input()))
    
cnt = 0

while len(arr) > 2 :
    #print("enter")
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)
    cnt += num1+num2
    tmp = num1+num2
    heapq.heappush(arr,tmp)
    print(arr)

if n == 1: # 반례 확인하기 - 1묶음이면 비교 ㄴㄴ임
    print(cnt)
else :
    print(sum(arr)+cnt)    
