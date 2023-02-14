nine = []
for _ in range(9):
    a = int(input())
    nine.append(a)
def printk(arr):
    arr.sort()
    for i in range(0,7):
        print(arr[i])
res=[]
for i in range(0,8):
    for j in range(i+1,9):
        b = nine.copy()
        b.remove(nine[i])
        b.remove(nine[j])
        if sum(b)==100:
            res = b.copy()
printk(res)
