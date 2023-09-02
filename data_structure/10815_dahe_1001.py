import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int,input().split()))
m = int(input())
sg = list(map(int,input().split()))

cards.sort()

def binary(left,right,ans):
    if ans == cards[left] : return 1
    elif ans == cards[right] : return 1
    elif left+1 == right : return 0
    else :
        center = int((left+right)/2)
        if cards[center] > ans : return binary(left,center,ans)
        elif cards[center] == ans : return 1
        else : return binary(center,right,ans)

res = [0]*m
for i in range(m):
    res[i] = binary(0,n-1,sg[i])
        
print(' '.join(map(str, res)))
