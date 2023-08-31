n = int(input())
dp = [1,1,1]

for _ in range(n):
    p = int(input())
    for i in range(len(dp),p):
        dp.append(dp[i-3]+dp[i-2])
    print(dp[p-1])
