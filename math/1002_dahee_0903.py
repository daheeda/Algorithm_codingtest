t = int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split()) #x y r x y r
    dist12 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if [x1,y1,r1] == [x2,y2,r2] : print(-1)
    elif min(x1+r1,x2+r2) == min(x1-r1,x2-r2): print(1)
    elif dist12+min(r1,r2) == max(r1,r2) : print(1)
    elif dist12 > r1+r2 : print(0)
    elif dist12+min(r1,r2) < max(r1,r2) : print(0)
    elif dist12 == r1+r2 : print(1)
    else : print(2)
