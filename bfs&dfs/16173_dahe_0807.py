n = int(input())
from collections import deque
que=deque()
arr=[]
for i in range(n):
    tmp = input().split(" ")
    arrt=[]
    for j in range(0,len(tmp)):
        arrt.append(int(tmp[j]))
    arr.append(arrt)

que.append([0,0])    
def jump(arr,ix,iy):
    if arr[iy][ix] == -1 :
        print('HaruHaru')
        return
    
    elif arr[0][0] == 0 :
        print('Hing')
        return
    
    else :
        if (arr[iy][ix] < n-ix) : # 오른쪽으로 이동 가능하다면
            if (arr[iy][ix+arr[iy][ix]] != 0) : # 이동하려는 곳이 0이 아니라면
                que.append([iy,ix]) # 현재위치 저장하고
                jump(arr,ix+arr[iy][ix],iy) # 이동함.
            else : # 이동하려는 오른쪽에 0이 있다면
                if (arr[iy][ix] < n-iy): # 아래쪽으로 이동할거야
                    if(arr[iy+arr[iy][ix]][ix] !=0 ): # 이동하려는 곳이 0이 아니라면
                        que.append([iy,ix]) # 현재 위치 저장하고
                        jump(arr,ix,iy+arr[iy][ix]) # 이동
                    else : # 이동하려는 곳 0이라면
                        arr[iy][ix] = 0 # 현재 위치도 0으로 바꾸고 (어느방향으로도 이동하지 못하는 경우임)
                        save=que.pop() # 이전경로로 돌아갈거야
                        jump(arr,save[1],save[0])
                else : # 아래쪽으로 이동 못하는 경우
                    arr[iy][ix]=0 # 현재 위치 0으로 바꾸고
                    save=que.pop() # 이전으로 돌아감
                    jump(arr,save[1],save[0])
            
        elif (arr[iy][ix] < n-iy): # 오른쪽으로 이동 못하고 아래쪽으로 이동 가능하다면
            if(arr[iy+arr[iy][ix]][ix] !=0 ): # 이동하려는 곳이 0이 아니라면
                que.append([iy,ix]) # 현재 위치 저장하고
                jump(arr,ix,iy+arr[iy][ix]) # 이동
            else : # 이동하려는 곳이 0이라면
                arr[iy][ix] = 0 # 위치 0으로 바꾸고
                save=que.pop() # 이전 위치로
                jump(arr,save[1],save[0]) # 돌아감.
            
        else : # 어느쪽으로도 이동 불가능하다면
            arr[iy][ix] = 0 
            save=que.pop() # 이전위치 되돌아감
            jump(arr,save[1],save[0])

jump(arr,0,0)
