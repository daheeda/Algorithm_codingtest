import sys
input=sys.stdin.readline
a,b = map(int,input().split())
L,R = 0,0
while a*b != 1 :
    if a<b : 
        b=b-a
        R +=1
    else : 
        a=a-b
        L +=1
print(L,R)
'''
a,b=tuple(map(int,input().split(' ')))
l=0
r=0

while a>1 and b>1:
    if a>b:
        l+=a//b
        a%=b
    else:
        r+=b//a
        b%=a
l += a-1
r += b-1
print(' '.join(map(str,[l,r])))
'''
