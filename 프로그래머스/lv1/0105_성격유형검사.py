def solution(survey, choices):
    answer = ''
    MBTI = ['R','T','C','F','J','M','A','N']
    MBTI_score=[0,0,0,0,0,0,0,0]
    score = [3,2,1,0,1,2,3]
    
    for i in range(0,len(survey)):
        ch1 = survey[i][0]
        ch2 = survey[i][1]
        if choices[i] > 4 :
            idx = MBTI.index(ch2)
            MBTI_score[idx] += score[choices[i]-1]
        elif choices[i] < 4 :
            idx = MBTI.index(ch1)
            MBTI_score[idx] += score[choices[i]-1]
    
    for i in range(0,8,2):
        if MBTI_score[i] >= MBTI_score[i+1]:
            answer += MBTI[i]
        else :
            answer += MBTI[i+1]
    
    return answer
