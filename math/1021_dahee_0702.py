from collections import deque
N,M = input().split(" ")
index = input().split(" ")
N=int(N)
M=int(M)
que = deque([i for i in range(1,N+1)])

cnt = 0
for i in range(0,M):
    val=int(index[i])
    if (que.index(val)) < (len(que)-que.index(val)) : # 왼 < 오
        cnt += que.index(val)
        for k in range(que.index(val)):
            que.rotate(-1)
        que.popleft()
    else :
        cnt += len(que)-que.index(val)
        for k in range(len(que)-que.index(val)):
            que.rotate(1)
        que.popleft()
print(cnt)
