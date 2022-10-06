import sys
from collections import deque
# arr=deque([1,2,3,4,5,6,7,8,9])
# arr.pop() # 오른쪽
# arr.popleft() # 왼쪽
# arr.append(10) # 오른쪽
# arr.appendleft(11) #왼쪽
# arr.rotate() 오른쪽으로 이동
# # 큐는 왼쪽으로 넣고 왼쪽으로 뺀다
time=int(input())
for i in range(time):
    n,m = map(int,input().split()) # 문서수, 궁금한문서 
    tmp = deque(list(map(int,input().split())))
    printer= deque([i for i in range(0,n)])
    cnt = 0
    while True :
        if tmp[0] == max(tmp) :
            cnt += 1
            if printer[0] == m :
                print(cnt)
                break
            tmp.popleft()
            printer.popleft()
        else : # rotate 방향은 크게 상관 없음
            save=tmp.popleft()
            tmp.append(save)
            save=printer.popleft()
            printer.append(save)