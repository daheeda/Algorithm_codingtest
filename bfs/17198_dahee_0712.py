from collections import deque

arr=[]
for i in range(10):
    tmp=input()
    tarr=[]
    for j in range(0,10):
        tarr.append(tmp[j])
    arr.append(tarr)

que = deque()

def bfs(arr,ix,iy,que,cnt) :
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    for i in range(0,4) :
        dx = x[i] + ix
        dy = y[i] + iy
        if (dx >= 0) & (dx < 10) & (dy >=0) & (dy < 10) :
            if arr[dy][dx] == '.' :
                arr[dy][dx] = cnt 
                que.append([dx,dy])    
            if arr[dy][dx] == 'L':
                return print(cnt)
    tmpxy=que.popleft()
    tmpx=tmpxy[0]
    tmpy=tmpxy[1]
    bfs(arr,tmpx,tmpy,que,arr[tmpy][tmpx]+1)

cnt = 0
for i in range(0,10):
    for j in range(0,10):
        if arr[i][j]=='B':
            bfs(arr, j, i, que, cnt)
