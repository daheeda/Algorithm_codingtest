import sys
n = int(input())
num = list(map(int,sys.stdin.readline().split()))
m = int(input())
num2 = list(map(int,sys.stdin.readline().split()))

res=""
num=set(num)

for i in range(0,m):
    try :
        num.remove(num2[i])
        res += "1 "
    except :
        res += "0 "
print(res)