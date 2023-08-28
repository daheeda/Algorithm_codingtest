n = int(input())
ai = list(map(int,input().split()))

dp = [0] * n
dp[0] = 1

for i in range(1,n):
    cnt = 0
    for j in range(0,i):
        if ai[i] > ai[j] :
            if cnt < dp[j] :
                cnt = dp[j]
    dp[i] = cnt + 1

print(max(dp))
