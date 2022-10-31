x=int(input())
dp = [x for _ in range(x+1)]
dp[1]=0
for index in range(1,x):
    if index*3 <= x :
        dp[index*3] = min(dp[index*3],dp[index]+1,index)
    if index*2 <= x :
        dp[index*2] = min(dp[index*2],dp[index]+1,index)
    dp[index+1] = min(dp[index+1],dp[index]+1,index)
print(dp[x])
