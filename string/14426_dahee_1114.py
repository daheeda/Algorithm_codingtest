import sys
input=sys.stdin.readline
n,m = map(int,input().split())
s=[]
for _ in range(n):
    s.append(input().strip())
cnt = 0
for _ in range(m):
    tmp = input().strip()
    for sent in s:
        if sent[:len(tmp)] == tmp :
            cnt += 1
            break
print(cnt)
