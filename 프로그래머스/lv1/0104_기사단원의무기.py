# 약수구하기
def solution(number, limit, power):
    if number == 1 :
        return 1
    else :
        answer = 1
        for i in range(2, number+1):
            cnt = 2 # 1과 자기 자신
            for j in range(2,int(i**0.5)+1):
                if i%j == 0:
                    cnt += 2
                    if j*j == i :
                        cnt -= 1
                        break
            if cnt > limit :
                answer += power
            else :
                answer += cnt
        return answer
