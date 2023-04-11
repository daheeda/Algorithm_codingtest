import math
k=int(input())
res=math.factorial(9+k)//(math.factorial(k)*math.factorial(9)) 
# /는 실수 나눗셈으로, 수가 커지면 정수 간의 나눗셈이라도 오차가 발생합니다.
print(int(res%10007))
