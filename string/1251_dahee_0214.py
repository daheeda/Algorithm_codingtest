s = list(input())
res = []
for i in range(1,len(s)-2):
    for j in range(len(s)-1,i,-1):
        res.append(s[0:i][::-1]+s[i:j][::-1]+s[j:len(s)][::-1])
print(''.join(min(res)))
