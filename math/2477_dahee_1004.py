k = int(input())
area = []
dirt = []
for _ in range(6):
    a, b = map(int,input().split())
    area.append(a)
    dirt.append(b)
    
for i in range(6):
    if (area[0] == area[2]) & (area[1] == area[3]):
        break
    else :
        pop_ = dirt[0]
        dirt = dirt[1:]
        dirt.append(pop_)
        pop_ = area[0]
        area = area[1:]
        area.append(pop_)

res = dirt[5]*dirt[4] - dirt[1]*dirt[2]
print(res*k)
