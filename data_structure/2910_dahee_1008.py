import sys
n,c = map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
tmp=[]
visit=[]
for i in range(0,n):
    cnt=arr.count(arr[i])
    if visit.count(arr[i]) == 0:
        tmp.append([cnt,n-i,arr[i]])
        visit.append(arr[i])
tmp.sort(reverse=True)
res=""
for i in range(0,len(tmp)):
    res += (str(tmp[i][2])+" ")*tmp[i][0]
print(res)
