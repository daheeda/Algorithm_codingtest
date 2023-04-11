import sys
input=sys.stdin.readline
n,m = map(int,input().split())
tree = list(map(int,input().split()))
res = 0
def cut(cur,high,under):
    global res
    cnt=0
    for i in range(0,len(tree)) :
        if tree[i]>cur :
            cnt = cnt + tree[i] - cur
        if cnt > m : break
    if cnt >= m :
        if cur > res :
            res = cur
            under = cur
            cur += (high-cur)//2
            cut(cur,high,under)
    else : 
        high=cur
        cur -= (cur-under)//2   
        if high != cur : cut(cur,high,under)

start = max(tree)//2
cut(start,max(tree),0)
print(res)
