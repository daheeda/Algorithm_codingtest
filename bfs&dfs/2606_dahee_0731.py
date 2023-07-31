from collections import deque
n = int(input())
m = int(input())
computer = []
visit = [0] * m
for _ in range(m):
    a,b = input().split()
    computer.append([int(a), int(b)])

n_list = [0]*n
n_list[0] = 1
que = [1]
que = deque(que)
    
def dpdp(arr,que,cnt):
    cur_computer = que.pop()
    for i in range(0,m):
        a = arr[i][0]
        b = arr[i][1]
        if visit[i] == 0:
            if a == cur_computer :
                que.append(b)
                visit[i]=1
                n_list[a-1] = 1
                n_list[b-1] = 1
            elif b == cur_computer:
                que.append(a)
                visit[i]=1
                n_list[b-1] = 1
                n_list[a-1] = 1
    
    if len(que) == 0 :
        return sum(n_list)
    else : return dpdp(arr,que,n_list)

print(dpdp(computer,que,n_list)-1)
