from itertools import permutations

n = int(input())
arrn = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
re = ['+']*a + ['-']*b + ['*']*c + ['//']*d
kk = arrn + re
resmax , resmin = -9999999999, 9999999999

def cal(ii,arrn):
    tmp = arrn[0]
    for i in range(len(ii)):
        if (ii[i] == '//') & (tmp < 0) :
            tmp = eval(str(abs(tmp))+ii[i]+str(arrn[i+1]))
            tmp *= (-1)
        else : tmp = eval(str(tmp)+ii[i]+str(arrn[i+1]))
    return tmp

for i in set(list(permutations(re,len(re)))):
    i = list(map(str,i))
    res = cal(i,arrn)
    if res >= resmax : resmax = res
    if res <= resmin : resmin = res
        
print(resmax)
print(resmin)
