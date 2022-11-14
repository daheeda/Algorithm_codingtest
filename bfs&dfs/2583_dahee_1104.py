def make(x1,y1,x2,y2) :
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[y][x] = -1 # color
        
from collections import deque
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
m,n,k = map(int,input().split())
arr=[ [0 for _ in range(n)] for _ in range(m)]
cnt = 1
res=[]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    make(x1,y1,x2,y2)

def search(ix,iy,cnt):
    x=[0,1,0,-1]
    y=[1,0,-1,0]
    for i in range(0,4):
        dx=x[i]+ix
        dy=y[i]+iy
        if (dx>=0) & (dy >=0) & (dx<n) & (dy<m) :
            if arr[dy][dx] == 0 :
                cnt += 1
                arr[dy][dx] = cnt
                que.append([dy,dx])
    if len(que) > 0 :
        ny,nx=que.popleft()
        return search(nx,ny,cnt) # 함수를 리턴해주자
# https://velog.io/@munang/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4
    else : return cnt

for y in range(0,m) :
    for x in range(0,n) :
        if arr[y][x] == 0 : 
            que=deque([])
            arr[y][x] = 1
            a=search(x,y,1)
            cnt+=1
            res.append(a)
print(cnt-1)
res.sort()
print(*res)
