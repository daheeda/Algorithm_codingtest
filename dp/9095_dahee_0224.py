n = int(input())

def dpdp(cur):
    dp[cur] += 1
    
    if cur+3 < tt :
        dpdp(cur+3)
        dpdp(cur+2)
        dpdp(cur+1)
        
    elif cur+2 < tt :
        dpdp(cur+2)
        dpdp(cur+1)
        
    elif cur+1 < tt :
        dpdp(cur+1)

for _ in range(n):
    tt = int(input())
    tt = tt+1
    dp = [ 0 for _ in range(tt)] 
    dpdp(0)
    print(dp[-1])
