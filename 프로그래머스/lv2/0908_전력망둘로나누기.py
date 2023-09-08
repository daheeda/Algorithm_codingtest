from collections import deque

def linked(arr,cur,res,que):
    
    for i in range(len(arr)):
        a = arr[i][0]
        b = arr[i][1]
        if a == cur :
            if res[b-1] == 0 :
                res[b-1] = 1
                que.append(b)
        elif b == cur :
            if res[a-1] == 0:    
                res[a-1] = 1
                que.append(a)
        
    if len(que)== 0 : return res
    else :
        ncur = que.popleft()
        return linked(arr,ncur,res,que)


def solution(n, wires):
    all_res = []
    for cut in range(len(wires)):
        
        tmp = wires.copy()
        del tmp[cut]
        res = [0] * n
        res[0] = 1
        que = deque([])
        res = linked(tmp,1,res,que)
        all_res.append(abs(res.count(1) - res.count(0)))
        
    return (min(all_res))
        
        
