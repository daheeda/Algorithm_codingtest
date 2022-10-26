n=int(input())
res=0
if n in [1,3]:
    print(-1)
else :
    if n%5 == 0:
        res = n//5
        print(res)
    elif n%5 == 1:
        res += n//5-1
        print(res+3)
    elif n%5 == 2:
        res += n//5
        print(res+1)
    elif n%5 == 3:
        res += n//5-1
        print(res+4)
    elif n%5 == 4:
        res += n//5
        print(res+2)
