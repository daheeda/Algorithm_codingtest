from collections import deque
import sys
sys.setrecursionlimit(100000)

def move(arr, visit, cnt, que, y, x, target):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if (nx >= 0) & (ny >= 0) & (nx < len(arr[0])) & (ny < len(arr)) :
            if visit[ny][nx] == 0 :
                if target == 'L' :
                    if arr[ny][nx] in ['S','E','O']:
                        visit[ny][nx] = cnt
                        que.append([ny,nx,cnt+1])
                    elif arr[ny][nx] == target :
                        return cnt
                if target == 'E' :
                    if arr[ny][nx] in ['S','O']:
                        visit[ny][nx] = cnt
                        que.append([ny,nx,cnt+1])
                    elif arr[ny][nx] == 'E':
                        return cnt+1
    if len(que) == 0 : return -1
    else :
        yy, xx, cnt2 = que.popleft()
        return move(arr,visit,cnt2,que,yy,xx,target)
        
def solution(maps):
    
    maps = [ x.replace('"','') for x in maps]
    레버, 출구 = 0,0
    for y in range(len(maps)):
        if maps[y].count('S') == 1:
            visit = [[0]*len(maps[0]) for _ in range(len(maps))]
            que = deque([])
            레버 = move(maps, visit, 1, que, y, maps[y].index('S'),'L')
            break
    if 레버 > 0 :
        for y in range(len(maps)):
            if maps[y].count('L') == 1:
                visit = [[0]*len(maps[0]) for _ in range(len(maps))]
                que = deque([])
                출구 = move(maps, visit, 레버, que, y, maps[y].index('L'),'E') 
                break
        return 출구
    else : return -1
    
        
        
        
        
    
    
    
