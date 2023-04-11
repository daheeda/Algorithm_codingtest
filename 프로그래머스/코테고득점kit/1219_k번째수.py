def solution(array, commands):
    runtime = len(commands)
    answer = []
    for i in range(runtime):
        a0 = commands[i][0]-1
        a1 = commands[i][1]
        a2 = commands[i][2]
        temp = array[a0:a1]
        temp.sort()
        answer.append(temp[a2-1])
    return answer
