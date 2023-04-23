n,m = map(int,input().split())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))
# 만족도 = a - b
alist.sort()
blist.sort()
res = 0
if n>=m :
    for i in range(0,m):
        tmp = alist[n-1-i]-blist[i]
        if tmp > 0 : res += tmp
        else : break
else : 
    for i in range(0,m-(m-n)):
        tmp = alist[n-1-i]-blist[i]
        if tmp > 0 : res += tmp
        else : break
print(res)
