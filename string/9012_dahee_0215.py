n = int(input())

def yn(a):
    if a.count("(") != a.count(")"):
        return False
    else :
        run = len(a)
        for _ in range(int(run/2)+1):
            a=a.replace("()","")
        if len(a)==0 : return True
        else : return False
for _ in range(n):
    s = input()
    if yn(s) : print("YES")
    else : print("NO")
    
