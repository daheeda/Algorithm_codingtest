n=int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split)))

while len(arr) > 1 :
    temp = [[0]*int(len(arr)/2) for _ in range(int(len(arr)/2))]
    for x in range(int(len(arr)/2)):
        for y in range(int(len(arr)/2)):
            div = [row[2*x:2*x+2] for row in arr[2*y:2*y+2]]
            div = sum(div, [])
            divmax = max(div)
            div.remove(divmax)
            temp[y][x] = max(div)
    arr = temp
    
print(arr[0][0])
