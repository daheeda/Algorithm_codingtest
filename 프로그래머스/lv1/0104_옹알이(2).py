def solution(babbling):
    answer = 0
    for bb in babbling :
        for k in range(15,1,-1):
            bb=bb.replace('aya'*k,'k')
            bb=bb.replace('ye'*k,'k')
            bb=bb.replace('woo'*k,'k')
            bb=bb.replace('ma'*k,'k')
        bb=bb.replace('aya','h')
        bb=bb.replace('ye','h')
        bb=bb.replace('woo','h')
        bb=bb.replace('ma','h')
        bb=bb.replace('h','') # 
        if bb == '':
            answer +=1
    return answer
