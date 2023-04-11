from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def fs(y,x,cnt):
    ix = [0,1,0,-1]
    iy = [1,0,-1,0]
    for i in range(0,4):
        dx = x + ix[i]
        dy = y + iy[i]
        if (dx>=0) & (dy >=0) & (dx<m) & (dy<n) :
            if (arr[dy][dx]==1) & (visit[dy][dx]==0) :
                visit[dy][dx] = cnt
                que.append([dy,dx])
    if len(que) > 0 :
        ny,nx=que.popleft()
        fs(ny,nx,cnt)

for _ in range(int(input())):
    m,n,k = map(int, input().split()) # x,y,배추개수
    arr=[[ 0 for _ in range(m)] for _ in range(n)]
    visit=[[ 0 for _ in range(m)] for _ in range(n)]
    for _ in range(k): 
        x,y = map(int,input().split())
        arr[y][x] = 1
    cnt = 0
    for y in range(0,n):
        for x in range(0,m):
            if (arr[y][x] == 1) & (visit[y][x] == 0):
                que=deque([])
                cnt += 1
                visit[y][x] = cnt
                fs(y,x,cnt)

    print(cnt)
