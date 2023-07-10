import sys
input = sys.stdin.readline

n = int(input())
nn = list(map(int,input().split(' ')))
m = int(input())
mm = list(map(int,input().split(' ')))

nn.sort()

def search(nnn, num, cur, start, end):
    
    if nnn[cur] == num :
        return print(1)
    elif start == end :
        return print(0)
    elif nnn[cur] < num :
        return search(nnn,num,int((end+cur)/2), cur+1, end)
    elif nnn[cur] > num :
        return search(nnn,num,int((cur)/2), start, cur)
    
for num in mm :
    search(nn, num, int(n/2), 0, n)
