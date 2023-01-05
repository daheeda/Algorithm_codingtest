def solution(s):
    answer = 0
    cntx=1
    cnty=0
    while len(s) > 0 :
        x = s[0]
        if len(s) >1 :
            for i in range(1,len(s)):
                y = s[i]
                if x == y :
                    cntx +=1
                else :
                    cnty += 1
                if cntx == cnty :
                    answer +=1
                    s = s[i+1:]
                    cntx=1
                    cnty=0
                    break
        if cntx+cnty == len(s):
            answer += 1
            s=''
    return answer
  # 재귀로 먼저 
