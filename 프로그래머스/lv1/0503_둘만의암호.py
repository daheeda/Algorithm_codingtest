def solution(s, skip, index):
    word = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z']
    word = [x for x in word if x not in skip] #순서 보존됨
    answer = ''
    for i in range(0,len(s)):
        start_idx = word.index(s[i])
        try : 
            answer += word[start_idx+index]
        except :
            answer += word[int((start_idx+index)%len(word))]
    return answer
