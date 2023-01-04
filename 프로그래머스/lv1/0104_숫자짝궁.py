def solution(X, Y):
    num = ['9','8','7','6','5','4','3','2','1','0']
    answer=''
    for i in num:
        #print(i)
        xc = X.count(i)
        yc = Y.count(i)
        ic = min(xc,yc)
        if ic > 0:
            answer = answer + str(i)*ic
    if answer == '':
        answer = '-1'
    if set(answer)== {'0'}:
        answer = '0'
        # 형변환은시간많이잡아먹는다!
    return answer
