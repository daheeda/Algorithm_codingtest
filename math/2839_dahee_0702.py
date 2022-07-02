N = int(input())

def sugar(N,temp):
    # 5의 배수인가?
    if (N%5) == 0 :
        print(int(N/5)+temp)
    # 정확하게 N키로그램을 만들수 없는가?
    elif N <3 :
        print(-1)
    # a*5 + b*3 으로 나타낼 수 있는가?
    else :
        sugar(N-3,temp+1)
        
sugar(N,0)
