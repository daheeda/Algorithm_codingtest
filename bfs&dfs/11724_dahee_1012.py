import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
linked=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
visited=[0 for i in range(N)]
tmp=deque([1])
visited[0]=1
def count(arr,visit,cnt):  
    if visit.count(0) > 0 :
        now=tmp.pop()
        for i in range(0,len(arr)):
            if arr[i][0] == now :
                if visit[arr[i][1]-1] == 0:
                    tmp.append(arr[i][1])
                    visit[arr[i][1]-1] = cnt
            elif arr[i][1] == now :
                if visit[arr[i][0]-1] == 0:
                    tmp.append(arr[i][0])
                    visit[arr[i][0]-1] = cnt
        if len(tmp) == 0 :
            cnt=cnt+1
            index=visit.index(0)
            tmp.append(index+1)
            visit[index]=cnt
            count(arr,visit,cnt)
        else :
            count(arr,visit,cnt)
    else : pass

if M != 0:
    count(linked,visited,1)
    print(max(visited))
else : print(N)
