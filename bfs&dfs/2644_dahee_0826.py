from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
p1,p2 = map(int,input().split())
m = int(input())

link = [ list(map(int,input().split())) for _ in range(m)]

visit = [0]*(n+1)

def dfs(cur, ans, cnt):
    
    if cur == ans : return cnt
    
    for i in range(0,m):
        if link[i][0] == cur:
            if visit[link[i][1]] == 0 :
                visit[link[i][1]] = cnt
                que.append([link[i][1],cnt+1])
        elif link[i][1] == cur:
            if visit[link[i][0]] == 0 :
                visit[link[i][0]] = cnt
                que.append([link[i][0],cnt+1])
            
    if len(que)== 0 : return -1
    else :
        ncur,ncnt = que.popleft()
        if ncur == ans : return visit[ans]-1
        else : return dfs(ncur,ans,ncnt)

que = deque()
visit[p1] = 1
print(dfs(p1,p2,2))
