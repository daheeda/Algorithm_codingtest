def solution(queue1, queue2):
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    want = (sum(queue1)+sum(queue2))/2
    s1 = sum(queue1)
    s2 = sum(queue2)
    while s1 != want :
        if s1>s2 :
            pp = queue1.popleft()
            queue2.append(pp)
            answer += 1
            s1 -= pp
            s2 += pp
        else :
            pp = queue2.popleft()
            queue1.append(pp)
            answer += 1
            s2 -= pp
            s1 += pp
        if answer > len(queue1)+len(queue2)+10:
            answer = -1
            break
    return answer
