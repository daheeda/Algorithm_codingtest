def solution(picks, minerals):
    answer = 0
    minerals = minerals[0:sum(picks)*5]
    sum_5 = [[minerals[5*i:5*i+5].count('diamond'),
              minerals[5*i:5*i+5].count('iron'),
             minerals[5*i:5*i+5].count('stone')] 
             for i in range(int(len(minerals)/5)+1)]
    sum_5.sort(reverse = True)
    for i in range(len(sum_5)):
        d,i,s = sum_5[i]
        if sum(picks) == 0 :
            break
        elif picks[0] > 0 :
            answer +=  (d*1 + i*1 + s*1)
            picks[0] -= 1
        elif picks[1] > 0 :
            answer += (d*5 + i*1 + s*1)
            picks[1] -= 1
        elif picks[2] > 0 :
            answer += (d*25 + i*5 + s*1)
            picks[2] -= 1

    return answer
