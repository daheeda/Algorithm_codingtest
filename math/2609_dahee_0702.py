a,b = input().split(" ")

a = int(a)
b = int(b)

def mx(num1,num2): # 유클리드
    a = max(num1, num2)
    b = min(num1, num2)
    if a%b == 0 :
        q = int(a/b -1)
    else :
        q = int(a//b)
    if a == b:
        print(a)
    else :
        mx(a-b*q,b)
        
def mn(num1,num2):
    a = max(num1, num2)
    b = min(num1, num2)
    for i in range(1,b+1):
        if i*a%b == 0 :
            print(i*a)       
            break
        
mx(a,b)
mn(a,b)
