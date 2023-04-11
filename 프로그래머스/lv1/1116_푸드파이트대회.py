def solution(food):
    answer = '0'
    for i in range(1,len(food)+1):
        plus = (food[-i])//2
        answer = str(len(food)-i)*plus+answer+str(len(food)-i)*plus
    return answer
