a= input()
b= input()
a1=[]
b1=[]
for i in range(0,len(a)):
    a1.append(a[i])
for i in range(0,len(b)):
    b1.append(b[i])

def make(a,b):
    if a == b : # 같은경우
        print(1) # 1 프린트
        return # 되는 경우
    else :
        if len(a)==len(b) : # 길이가 같아지면
            print(0)
            return # 안되는경우
        else :
            if b[len(b)-1] == 'B':
                b.pop() # b를 지운다
                b.reverse()
                make(a,b) # 재귀에러 발생하는 이유는?
            elif b[len(b)-1] == 'A':
                b.pop()
                make(a,b) # 재귀에러 발생하는 이유는?
            else :
                print(0)
                return

make(a1,b1)
