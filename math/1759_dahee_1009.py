from itertools import combinations
l,c = map(int,input().split())
alph = list(input().split())
p1 = ['a', 'e', 'i', 'o', 'u']
alph.sort()
res = []

for i in list(combinations(alph,l)):
    cnt = 0
    word = ''.join(i)
    for w in word:
        if w in p1 : cnt += 1
    if cnt >= 1 :
        if len(word)-cnt >= 2 :
            res.append(word)

for i in res : print(i)
