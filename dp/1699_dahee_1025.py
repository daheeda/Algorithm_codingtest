n = int(input())
arr = [i*i for i in range(1,int(n**0.5)+1)]
dp = [i for i in range(0,n+1)]

for i in range(4,n+1):
    for j in range(1,int(i**0.5)):
        dp[i] = min(dp[i],1+dp[i-arr[j]])
print(dp[n])
