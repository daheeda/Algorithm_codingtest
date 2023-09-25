n,m = map(int, input().split())

nlist = {input() for _ in range(n)}
mlist = [input() for _ in range(m)]
res = 0

for i in mlist:
    if i in nlist :
        res += 1

print(res)
