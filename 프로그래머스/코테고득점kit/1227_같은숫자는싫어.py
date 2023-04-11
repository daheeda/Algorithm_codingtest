def solution(arr):
    answer = []
    for j in range(0,len(arr)) :
        i = arr[j]
        if len(answer) == 0 :
            answer.append(i)
        elif answer[len(answer)-1] != i:
            answer.append(i)
    return answer
