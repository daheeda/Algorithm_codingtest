def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    center = [2,5,8,0]
    answer = ''
    leftpos = [3,0]
    rightpos =[3,2]
    for i in numbers :
        if i in left :
            answer += 'L'
            leftpos = [left.index(i),0]
        elif i in right :
            answer += 'R'
            rightpos = [right.index(i),2]
        else :
            lp = abs(center.index(i)-leftpos[0]) + abs(leftpos[1]-1)
            rp = abs(rightpos[0]-center.index(i)) + abs(rightpos[1]-1)
            if  lp > rp:
                answer += 'R'
                rightpos = [center.index(i),1]
            elif lp < rp:
                print("here")
                answer += 'L'
                leftpos = [center.index(i),1]
            else :
                if hand=='right':
                    answer +='R'
                    rightpos = [center.index(i),1]
                else : 
                    answer += 'L' 
                    leftpos = [center.index(i),1]
    return answer
