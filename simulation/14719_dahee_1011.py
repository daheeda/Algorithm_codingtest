h,w = map(int,input().split())
block = list(map(int,input().split()))

res, left, right = 0, 0, len(block)-1

while True :
    if block[left] >= block[right] :
        for i in range(left,right+1):
            if block[i] < block[right] :
                res += block[right] - block[i]
                block[i] = block[right]
        right -= 1
    else:
        for i in range(left,right+1):
            if block[i] < block[left] :
                res += block[left] - block[i]
                block[i] = block[left]
        left += 1
    if right == left : break

print(res)
