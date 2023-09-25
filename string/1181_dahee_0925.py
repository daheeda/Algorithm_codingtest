import sys
input = sys.stdin.readline

n = int(input().strip())
words = [ input().strip() for _ in range(n)]
words = list(set(words))
words.sort()
res = []


'''
words.sort(key=len)  <- 이거 하나면 for 문 없어두 댐.......;;;
'''

for i in range(51):
    for word in words :
        if len(word)==i:
            res.append(word)
            
for i in res : print(i)
