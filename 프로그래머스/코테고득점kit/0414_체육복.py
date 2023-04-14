def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    stu = [1] * (n+2)
    stu2 = [0] * (n+2)
    for ls in lost : stu[ls]=0
    for rs in reserve :
        if stu[rs] == 1:
            if rs > 1 :
                if (stu[rs-1] == 0) & (stu2[rs-1]==0):
                    stu2[rs-1] = 1
                elif (stu[rs+1] == 0) & (stu2[rs+1]==0):
                    stu2[rs+1] = 1
            elif rs == 1 :
                if (stu[rs+1] == 0) & (stu2[rs+1]==0):
                    stu2[rs+1] = 1
        else : stu2[rs] = 1
    stu2[0] = 0
    stu2[-1] = 0
    stu[0] = 0
    stu[-1] = 0
    answer += (stu.count(1))
    answer += (stu2.count(1))
    return answer
