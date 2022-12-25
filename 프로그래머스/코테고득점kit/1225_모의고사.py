def solution(answers):
    
    import numpy as np

    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    ans_len = len(answers)
    answers = np.array(answers)
    answer = []
    
    n1 = np.array((n1*ans_len)[:ans_len])
    n2 = np.array((n2*ans_len)[:ans_len])
    n3 = np.array((n3*ans_len)[:ans_len])
    
    tf1 = n1==answers
    tf2 = n2==answers
    tf3 = n3==answers
    
    s1 = len(tf1[tf1 == True])
    s2 = len(tf2[tf2 == True])
    s3 = len(tf3[tf3 == True])
            
    winner = max(s1,s2,s3)
    
    if s1 == winner :
        answer.append(1)
    if s2 == winner :
        answer.append(2)
    if s3 == winner :
        answer.append(3)
        
    return answer
