n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(input())

res = ''
cnt = 0

dna = ['A','T','G','C']

for i in range(m):
    tmp = [0,0,0,0]
    for j in range(n):
        tmp[dna.index(arr[j][i])] += 1
    res += dna[tmp.index(max(tmp))]
    cnt += (n-max(tmp))
    
print(res)
print(cnt)
