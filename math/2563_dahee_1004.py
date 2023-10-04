n = int(input()) #색종이 수

white = [[0]*101 for _ in range(101)]

for _ in range(n):
    x1, y1 = map(int,input().split())
    x2 = x1+10
    y2 = y1+10
    for x in range(x1,x2):
        for y in range(y1,y2):
            white[x][y] = 1

print(sum(sum(white[i]) for i in range(len(white))))
