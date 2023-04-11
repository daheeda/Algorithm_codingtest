G = input()
G = int(G)
arr = [(i**2)+G for i in range(1,100000)] 
poss = []

for i in range(0,len(arr)):
    if arr[i]**(1/2) == int(arr[i]**(1/2)): # 자연수의 제곱값인지 확인
        poss.append(arr[i]**(1/2))

if len(poss)==0:
    print(-1)
else :
    for i in range(0,len(poss)):
        print(int(poss[i]))
