t = int(input())

for _ in range(t):
    
    p = input().replace('RR','')
    n = int(input())
    num = input()[1:-1].split(',')
    if (n > 0):
        r = 0 # forward
        num = list(map(int,num))
        res = ''
        for i in p :
            if i == 'R': r = (r+1)%2
            else :
                if len(num)>0 : 
                    if r == 0 :num.pop(-len(num))
                    else : num.pop()
                else :
                    res = 'error'
                    break
        if res == 'error' : print(res)
        else : 
            if r == 0 : print(str(num).replace(' ',''))
            else : 
                num.reverse()
                print(str(num).replace(' ',''))
    else : 
        if p.count('D') > 0: print('error')
        else : print('[]')
    
