import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
tree=[ [] for i in range(0,n+1)] # 출력리스트
res = [ 0 for i in range(0,n+1)]
que=deque([]) # 큐
node = 1

for i in range(0,n-1) :
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
root = 1        
for i in range(0,len(tree[1])):
    que.append([tree[1][i],root])
    res[tree[1][i]] = root

while len(que) != 0:
    save=que.popleft()
    tmp = save[0]
    root = save[1]
    tree[root].remove(tmp)
    for i in range(0,len(tree[tmp])) :
        if tree[tmp][i] == root :
            continue
        else : 
            que.append([tree[tmp][i],tmp])
            res[tree[tmp][i]] = tmp
            #tree[tmp].remove(tree[tmp][i])
            
for i in range(2,len(res)):
    print(res[i])
