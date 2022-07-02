num = int(input()) # 입력

fibo = [0,1]

for i in range (0,num-1):
    fibo.append(fibo[i]+fibo[i+1])

print(fibo[num])
