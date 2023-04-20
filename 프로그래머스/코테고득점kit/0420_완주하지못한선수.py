def solution(participant, completion):
    answer = set(participant) - set(completion)
    try : return answer.pop()
    except : 
        for name in completion :
            if participant.count(name) > completion.count(name) :
                return name
