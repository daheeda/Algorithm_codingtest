##print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)

n = int(input())
arr = [input() for _ in range(n)]

res = 0

for i in range(n):
    cnt = [arr[i][0]]
    i_cnt = 1
    for j in range(1,len(arr[i])):
        
        if arr[i][j] == arr[i][j-1]:
            i_cnt += 1
            continue
        else :
            if arr[i][j] in cnt : break
            else : 
                cnt.append(arr[i][j])
                i_cnt += 1
                
    if i_cnt == len(arr[i]):
        res += 1
                
print(res)
