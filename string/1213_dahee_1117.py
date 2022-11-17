from collections import Counter
import sys
input=sys.stdin.readline
s=list(input().strip())
s.sort()
counter = Counter(s)
tf = 0
res = []
if len(s) % 2 == 0:
    for k in counter.keys():
        if counter[k] % 2 == 1:
            tf = 1
            break
    if tf == 0 :
        for k in counter.keys():
            for _ in range(counter[k]//2) :
                res.append(k)
        res2 = res.copy()
        res2.sort(reverse=True)
        print(''.join(res+res2))
    else : print("I'm Sorry Hansoo")    
else :
    odd=[]
    for k in counter.keys():
        if counter[k] % 2 == 1:
            tf +=1
            odd.append(k)
        if tf == 2 :
            break
    if tf == 1 :
        for k in counter.keys():
            for _ in range(counter[k]//2) :
                res.append(k)
        res2 = res.copy()
        res2.sort(reverse=True)
        print(''.join(res+odd+res2))
    else : print("I'm Sorry Hansoo")
