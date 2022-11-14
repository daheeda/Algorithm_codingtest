from collections import deque

n,m = map(int, input().split())#  y, x
arr=[list(map(int,input()))for _ in range(n)]
que=deque([])

for i in range(0,m):
    if arr[0][i] == 0 :
        arr[0][i]=-1
    que.append([arr[0][i],0,i]) # 값, y, x
while len(que) != 0:
    ix=[0,1,-1,0]
    iy=[1,0,0,-1]
    tmp=que.popleft()
    if tmp[0] == -1 :
        arr[tmp[1]][tmp[2]] = -1 #이동가능지역임
        for i in range(0,4) :
            dx=ix[i]+tmp[2]
            dy=iy[i]+tmp[1]
            if (dx>=0) &(dy>=0) &(dx<m ) &(dy<n):
                if arr[dy][dx] == 0 :
                    arr[dy][dx] = -1 # 이동완료
                    que.append([-1,dy,dx])
if arr[n-1].count(-1) == 0 :
    print("NO")
else : print("YES")
