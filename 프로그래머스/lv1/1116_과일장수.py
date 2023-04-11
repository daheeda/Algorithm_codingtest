def solution(k, m, score):
    score.sort()
    res = 0
    for i in range(1,len(score)//m+1):
        res += score[-i*m]*m
    answer=res
    return answer
