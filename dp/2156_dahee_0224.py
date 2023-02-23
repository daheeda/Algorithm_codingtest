import sys
sys.setrecursionlimit(10**8) # 재귀 에러나면 재귀 깊이 늘려주기
n = int(input())
value = [0] 
dp = [0]*(n+1)

for _ in range(n):
    num = int(input())
    value.append(num)
    
def dpdp(cur): # 현재 위치에서 max return
    if cur < n+1 :
        dp[cur] = max(dp[cur-2]+value[cur], dp[cur-1], dp[cur-3]+value[cur-1]+value[cur])
        dpdp(cur+1)

dpdp(1)
print(max(dp))
