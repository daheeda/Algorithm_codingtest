#1932#누적합!!
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
nlist=[[arr[0][0]]]
for i in range(1,n):
    tmp=[]
    for j in range(0,len(arr[i])):
        if j == 0 :
            k=arr[i][j]+nlist[i-1][j] # 시작
        elif j == len(arr[i])-1 :
            k=arr[i][j]+nlist[i-1][j-1] # 끝
        else :
            k=arr[i][j]+max(nlist[i-1][j-1:j+1]) #중간
        tmp.append(k)
    nlist.append(tmp)
print(max(nlist[n-1]))
