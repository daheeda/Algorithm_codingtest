import sys
time=int(input())
arr=[ int(sys.stdin.readline()) for i in range(time)]
stack=[1]
value=1
res=["+"]
for i in range(0,time):
    now=arr[i]
    while True :
        try : # stack 비어있지 않음.
            tmp = stack.pop()
            if tmp == now :
                res.append("-") # pop
                break
            else :
                stack.append(tmp) # pop한거 취소
                value += 1
                if value > time :
                    res.append("no")
                    break
                else :
                    res.append("+") # push
                    stack.append(value)
        except :
            value += 1
            if value > time :
                res.append("no")
                break
            else :
                res.append("+") # push
                stack.append(value)
            
                
if res.count("no") == 0 :
    for i in range(0,len(res)):
        print(res[i])
else : print("NO")
