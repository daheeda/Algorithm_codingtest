import sys
sys.setrecursionlimit(100000) #재귀에러시추가
from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
root=deque()

def find_rute(arr,x,y,root,cnt,n,m):
    ix=[0,1,0,-1]
    iy=[1,0,-1,0]
    for i in range(0,4):
        dx = x + ix[i]
        dy = y + iy[i]
        if (dx>=0)&(dy>=0)&(dx<m)&(dy<n):
            if arr[dy][dx] == 1 : # 이동가능한경우
                arr[dy][dx] = cnt+1
                root.append((dy,dx,cnt+1))
    if len(root) == 0 : pass
    else : 
        ny,nx,ncnt=root.popleft()
        find_rute(arr,nx,ny,root,ncnt,n,m)
    
find_rute(graph,0,0,root,1,N,M)
print(graph[N-1][M-1])
