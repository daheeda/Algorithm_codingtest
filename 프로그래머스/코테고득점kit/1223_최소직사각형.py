def solution(sizes):
    answer = 0
    ax = 0 # 더 작은거
    ay = 0 
    for i in sizes :
        v1 = i[0]
        v2 = i[1]
        if v1 > v2 :
            if v2 > ax :
                ax = v2
            if v1 > ay :
                ay = v1
        else :
            if v2 > ay :
                ay = v2
            if v1 > ax :
                ax = v1
    answer = ax*ay
    return answer
