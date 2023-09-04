'''import sys
input = sys.stdin.readline

n = int(input()) # 구매하려는 카드의 개수
pay = list(map(int,input().split()))

pay.insert(0,0)
dp = pay.copy()

for i in range(1,n+1):
    for j in range(0,i):
        if i%2 == 0: dp[i] = max(dp[i-j]+dp[j],dp[int(i/2)]*2, dp[i])
        else :dp[i] = max(dp[i-j]+dp[j], dp[i])
    
print(dp[-1])'''

import sys
input = sys.stdin.readline

n = int(input()) # 구매하려는 카드의 개수
dp = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(0,i):
        dp[i] = max(dp[i-j]+dp[j], dp[i])
    
print(dp[-1])
