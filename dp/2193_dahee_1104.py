n=int(input())
# 1 -> 1
# 2 -> 10
# 3 -> 100, 101 # 1번에서 앞에 10 추가한거 + 0인거
# 4 -> 1010, 1000, 1001 # 2번에서 앞에 10추가한거 + 1번에서 앞에 100 추가한거 + 0인거
# 5 -> 10100, 10101, 10010, 10001, 10000 # 3번에서 앞에 10 추가한거 + 2번에서 앞에 100 추가한거 + 1번에서 앞에 1000 추가한거 + 0 인거
# ...
# f(5) =f(3) + f(2) + f(1) +1
# f(4) =f(2) + f(1) + 1
# f(3) = f(1) +1
# f(1) = f(2) = 1
f=[1,1]
for _ in range(2,n) :
    f.append(sum(f[:-1])+1)
    
print(f[n-1])