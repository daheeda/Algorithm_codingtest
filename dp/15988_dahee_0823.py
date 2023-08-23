import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*1000000
dp[0],dp[1],dp[2]=1,2,4
for _ in range(n):
    s = int(input())
    if dp[s-1] != 0 :
        print(dp[s-1])
    else :
        for i in range(dp.index(0),s):
            dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009
        print(dp[s-1])
