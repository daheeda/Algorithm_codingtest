def solution(n, k):
    import math
    answer=[]
    num = [i for i in range(1,n+1)]
    for i in range(1,n+1):
        cnt = 0
        while k > math.factorial(n-i):
            k = k - math.factorial(n-i)
            cnt += 1
        answer.append(num[cnt])
        num.remove(num[cnt])
    return answer
