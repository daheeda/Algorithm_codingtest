n,m = map(int,input().split())
BW = ['B','W']
startb = [ BW[i%2] for i in range(0,8)]
startw = [ BW[i%2] for i in range(1,9)]
arr = []

for _ in range(n):
    x = input()
    arr.append(list(''.join(x)))
    
def returncnt(arr):
    bcnt = 0
    for i in range(0,8):
        for j in range(0,8):
            if i%2 == 0 : # startb
                if arr[i][j] != startb[j]:
                    bcnt +=1
            else :
                if arr[i][j] != startw[j]:
                    bcnt +=1
    wcnt = 0
    for i in range(0,8):
        for j in range(0,8):
            if i%2 == 0 : # startb
                if arr[i][j] != startw[j]:
                    wcnt +=1
            else :
                if arr[i][j] != startb[j]:
                    wcnt +=1
    return min(wcnt,bcnt)

res = []
for y in range(0,n-8+1):
    for x in range(0,m-8+1):
        narr = [row[x:x+8] for row in arr[y:y+8]]
        res.append(returncnt(narr))
print(min(res))
