import sys
input = sys.stdin.readline

n,m = map(int,input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
        
dp = [[0]*(m+1) for _ in range(n+1)]

for x in range(0,m-1):
    for y in range(0,n-1):
        dp[y+1][x] = dp[y][x] + miro[y+1][x]
        dp[y][x+1] = dp[y][x] + miro[y][x+1]

for x in range(0,m):
    for y in range(0,n):
        dp[y][x] = max(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + miro[y][x]
        
print(dp[n-1][m-1])
