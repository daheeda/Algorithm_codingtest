from itertools import permutations
def solution(numbers):
    s = list(numbers)
    arr2 = []
    for i in range(1,len(s)+1):
        arr2 += list(map(''.join, permutations(s,i)))
    arr2 = list(map(int,arr2))
    arr2 = set(arr2)
    res = 0  #len(arr2)
    for num in arr2:
        cnt = 0
        for i in range(2,int(num**(0.5)+0.5)+1):
            if num % i == 0 :
                cnt += 1
                break
        if cnt == 0:
            if (num != 1) & (num !=0) :
                res += 1
    return res
