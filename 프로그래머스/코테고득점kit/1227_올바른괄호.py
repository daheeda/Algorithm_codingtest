def solution(s):
    answer = True
    arr=[]
    for i in s :
        if i == '(' :
            arr.append(i)
        else :
            if len(arr)==0 :
                answer = False
                break
            elif arr[-1] == '(':
                arr.pop()
    if len(arr)!=0:
        answer = False
    return answer
