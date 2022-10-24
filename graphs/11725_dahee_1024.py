import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
arr=[]
tree=[ [] for i in range(0,n+1)]
res = [ 0 for i in range(0,n+1)]# 출력리스트
que=deque([]) # 큐

for i in range(0,n-1) : # 입력받기
    tmp = list(map(int,input().split()))
    arr.append(tmp)
    a=tmp[0]
    b=tmp[1]
    tree[a].append(b) # 연결된 모든 노드 저장
    tree[b].append(a)
    
root = 1        
for i in range(0,len(tree[1])): # 루트노드 큐에 넣기
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
            
for i in range(2,len(res)):
    print(res[i])
