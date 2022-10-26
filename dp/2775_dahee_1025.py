import math
t=int(input()) # test case
test=[]
# 0층 i호  i명 거주
for _ in range(t) :
    k=int(input()) # k 층
    n=int(input()) # n 호
    kf=math.factorial(k+1)
    nf=math.factorial(n-1)
    knf=math.factorial(n+k)
    print(int(knf/(kf*nf)))
