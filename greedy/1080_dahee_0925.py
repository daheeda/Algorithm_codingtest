n,m = map(int,input().split())

a = [list(map(int,input())) for _ in range(n)]
b = [list(map(int,input())) for _ in range(n)]

if a==b : print(0)
elif (n<3)|(m<3) : print(-1)
else :
    res = 0
    for y in range(n-3+1):
        for x in range(m-3+1):
            if a[y][x] == b[y][x] : continue
            else :
                res += 1
                for ny in range(y,y+3):
                    for nx in range(x,x+3):
                        if a[ny][nx] == 1 : a[ny][nx] = 0
                        else : a[ny][nx] = 1
    if a==b :print(res)
    else : print(-1)
