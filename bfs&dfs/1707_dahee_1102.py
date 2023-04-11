from collections import deque
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    V,e = map(int,input().split())
    visit=[ -1 for _ in range(V+1)]
    res = True
    arr=[[] for _ in range(V+1)]
    que = deque([])
    for _ in range(e) :
        u,v = map(int,input().split())
        arr[u].append(v)
        arr[v].append(u)
    for k in range(1,V+1):
        if visit[k] == -1 :
            que.append(k)    
            while len(que) !=0:
                pnode=que.popleft()
                for cnode in arr[pnode] :
                    if visit[cnode] == -1 :
                        visit[cnode] = (visit[pnode]+1)%2
                        que.append(cnode)
                    else :
                        if visit[cnode] == visit[pnode]:
                            res = False
                            que.clear()
    if res : print("YES")
    else : print("NO")
