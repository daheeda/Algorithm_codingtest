s = int(input())

s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))

s1.sort()
s2.sort(reverse=True)

res = 0
for i in range(s):
    res += s1[i]*s2[i]
    
print(res)
