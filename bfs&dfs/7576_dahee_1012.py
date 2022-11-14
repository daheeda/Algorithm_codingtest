import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
tmp = deque([])
cnt = 0
for i in range(0,m):
    for j in range(0,n):
        if arr[i][j] == 1:
            tmp.append([i,j,1]) # y,x,cnt

while len(tmp) > 0 :
    ny,nx,ncnt = tmp.popleft() # que
    ix = [0,1,0,-1]
    iy = [1,0,-1,0]
    for i in range(0,4) :
        dx = ix[i]+nx
        dy = iy[i]+ny
        if (dx>=0) & (dy>=0) & (dx<n) & (dy<m):
            if arr[dy][dx] == 0 :
                arr[dy][dx] = ncnt+1
                tmp.append([dy,dx,ncnt+1])
res=0
for i in range(0,m):
    for j in range(0,n):
        if arr[i][j] == 0:
            res = 1
            break
if res == 0:
    print(ncnt-1)
else : print(-1)
