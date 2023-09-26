import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a = {input().strip() for _ in range(n)}
#b = [ input() for _ in range(m)]
res = []

for _ in range(m):
    kk = input().strip()
    if kk in a :
        res.append(kk)

res.sort()
print(len(res))
for name in res:
    print(name)
