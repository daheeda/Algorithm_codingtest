from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
range_list = set(sum(area,[]))
    
dx = [-1,0,1,0]
dy = [0,-1,0,1]
    
def bfs(visit,y,x,dp):
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (nx>=0)&(ny>=0)&(nx<n)&(ny<n):
            if visit[ny][nx] == 0:
                if area[ny][nx] > dp :
                    visit[ny][nx] = 1
                    que.append([ny,nx])
    
    if len(que)==0:
        return visit
    else:
        yy,xx = que.popleft()
        return bfs(visit,yy,xx,dp)

res = [1]
for dp in range_list:
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if area[y][x] > dp :
                if visit[y][x] == 0:
                    que = deque()
                    visit = bfs(visit,y,x,dp)
                    cnt += 1
    res.append(cnt)
print(max(res))
