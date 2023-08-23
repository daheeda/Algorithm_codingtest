from collections import deque

arr = []
for _ in range(19):
    line = list(map(int,input().split()))
    arr.append(line)

visit = [
    [[0] * 19 for _ in range(19)],  # 우
    [[0] * 19 for _ in range(19)],  # 우하
    [[0] * 19 for _ in range(19)],  # 하
    [[0] * 19 for _ in range(19)],  # 우상
]

def baduk(x,y,color,n,que,arr,d):
    
    dx = [1,1,0,1] 
    dy = [0,1,1,-1]  
    
    ix = x + dx[d]
    iy = y + dy[d]
    
    if (ix>=0) & (ix<19) & (iy>=0) & (iy<19) : # 이동가능한경우
        if arr[iy][ix]==color:
            if visit[d][iy][ix] == 0:
                que.append([ix,iy,color])
                visit[d][iy][ix] = n+1 
                    
    if len(que) > 0 :
        nx, ny, color = que.popleft()
        return baduk(nx,ny,color,n+1,que,arr,d)
    else : return n
    
px, py, pw = 0, 0, 0

for x in range(0,19):
    for y in range(0,19):
        if pw == 0 :
            for d in range(4):
                if arr[y][x] == 0 :
                    continue
                else :
                    que = deque([])
                    tmp = baduk(x,y,arr[y][x],2,que,arr,d)
                    if tmp == 6 : px, py, pw = x , y, arr[y][x]
                        
if pw != 0 : print(pw,'\n',py+1,' ', px+1,sep='')
else : print(0)
