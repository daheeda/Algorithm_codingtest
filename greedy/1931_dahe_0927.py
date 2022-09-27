n = int(input())
arr=[]

for i in range(n) :
    s,f=input().split(" ") 
    arr.append([int(f),int(s)]) # 끝 / 시간

arr.sort() # 
end=arr[0][0]
cnt = 1
for i in range(1,n):
    if arr[i][1] >= end :
        end = arr[i][0]
        cnt += 1
print(cnt)
