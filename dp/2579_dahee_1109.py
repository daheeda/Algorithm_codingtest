n=int(input())
stair=[ int(input()) for _ in range(n)]
dp = [0 for _ in range(0,n+3)] 

if n >=3 :
    dp[1] = stair[0]
    dp[2] = max(stair[1], dp[1]+stair[1])
    for cur in range(3,n+1):
        #             직전계단 밟고 왔다                     직전계단 노노
        dp[cur] = max(dp[cur-3]+stair[cur-1]+stair[cur-2] , dp[cur-2]+stair[cur-1])
    print(dp[n])
elif n == 2:
    print(stair[0]+stair[1])
else :
    print(stair[0])
    # https://daimhada.tistory.com/181
