import sys
input = sys.stdin.readline
n=int(input())
tp=[list(map(int,input().split()))for _ in range(n)] 
tp.append([0,0])
dp=[ 0 for i in range(0,n+1)] 
for i in range(0,n+1) :# i 는 인덱스 기준 일 시작하는 날짜. 0일부터 n일까지(n=퇴사하는··날)
    t=tp[i][0] # time
    p=tp[i][1] # pay
    if i+t <= n : # 퇴사일까지 일 가능
        day = i+t # 인덱스 기준 정산받는 날짜.
        dp[day] = max(dp[day],max(dp[:i+1])+p)   # 기존값 vs 새로운 값
        
print(max(dp))
