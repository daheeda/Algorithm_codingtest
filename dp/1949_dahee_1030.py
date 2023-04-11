import sys
sys.setrecursionlimit(10**8) # 재귀 에러나면 재귀 깊이 늘려주기
input=sys.stdin.readline
n=int(input())
people=list(map(int,input().split()))
dp=[[0,0] for _ in range(0,n+1)]
tree=[[] for _ in range(0,n+1)]
for i in range(0,n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
visit= [True]*(n+1)

def dpdp(cur) :
    # 방문의 끝으로 거슬러 올라가 max 값을 계속 바꿔주겠다.
    dp[cur][0] = people[cur-1]
    dp[cur][1] = 0
    visit[cur] = False # 이제 방문 못한다.
    
    for nxt in tree[cur]: # cur 과 연결된 노드
        if visit[nxt] : # 방문전이면 해당 노드에서의 max 찾아주어야 함.
            dpdp(nxt) # 재귀 ; 새로운 노드로 들어가서 돌리겠음.    
            # 재귀에서 나오게되면
            dp[cur][0] += dp[nxt][1]# 우수마을
            dp[cur][1] += max(dp[nxt][0],dp[nxt][1])# 일반마을
        
dpdp(1)
print(max(dp[1]))
