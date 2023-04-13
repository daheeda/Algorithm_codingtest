from collections import deque

def make_100(pro, speeds):
    while pro[0] < 100 :
        for i in range(0,len(pro)):
            pro[i] += speeds[i]
    return pro, speeds

def solution(progresses, speeds):
    leng = len(speeds)
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while sum(answer) < leng :
        progresses, speeds = make_100(progresses, speeds)
        res = 0
        while progresses[0] > 99 : 
            if len(progresses) == 1 : 
                res += 1
                break
            else :
                progresses.popleft()
                # arr.pop(0) 이거 
                speeds.popleft()
                res += 1
        answer.append(res)
    return answer
