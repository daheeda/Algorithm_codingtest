from collections import deque

def solution(plans):
    answer = []
    plans.sort(key=lambda x: (x[1]))
    subject = deque([ i[0] for i in plans ])
    start = deque([ int(i[1].split(':')[0])*60 + int(i[1].split(':')[1]) for i in plans ])
    left = deque([ int(i[2]) for i in plans ])
    tmp = deque([])
    interval = deque([start[i]+left[i] - start[i+1] for i in range(len(start)-1)])
    interval.append(0)
    while len(subject) > 0 :
        if interval[0] <= 0 : # 깔끔하게 끝냄
            res = subject.popleft()
            start.popleft()
            kk = interval.popleft()
            answer.append(res)
            while len(tmp) > 0 : # interval 사이에 남은 과제 하는 경우
                if abs(kk) >= abs(tmp[-1][1]) : # 남은 과제 끝내는 경우
                    answer.append(tmp[-1][0])
                    kk += tmp[-1][1]
                    tmp.pop()
                else : 
                    tmp[-1][1] -= abs(kk)
                    break
        else : # 과제 미루고 새로운거 시작하는 경우
            res1 = subject.popleft()
            start.popleft()
            res4 = interval.popleft()
            tmp.append([res1,res4])
            
    for i in range(len(tmp)):
        kk = tmp.pop()
        answer.append(kk[0])
        
    return answer




'''ㄷㄷ;;
def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))
    '''
