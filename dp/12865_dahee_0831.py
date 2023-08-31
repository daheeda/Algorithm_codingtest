n,k = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(n)]

# dp[i][j] = j개의 무게를 가방에 담을 수 있을 때, i개의 물건 중 담을 수 있는 최대 가치??
# dp[물건][무게] : 무게가 j 일때, i물건을 담을 수 있는경우와 없는 경우중 최대값??
column_sum = sum(row[0] for row in wv)
if column_sum < k :
    k = column_sum

dp = [[0]*(k+1) for _ in range(n+1)]

for j in range(1,k+1): # 제한
    for i in range(n): # 무게
        if wv[i][0] > j :
            dp[i+1][j] = dp[i][j]
        else :
            #print(j, dp[i-1][j-wv[i][0]], wv[i][0], wv[i][1], dp[i-1][j])
            dp[i+1][j] = max(dp[i][j-wv[i][0]] + wv[i][1], dp[i][j])

print(dp[n][k])
