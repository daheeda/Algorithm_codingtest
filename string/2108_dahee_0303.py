import sys
input = sys.stdin.readline
from collections import Counter

n= int(input())
arr=[]

for _ in range(n):
    arr.append(int(input()))

arr.sort()

def 중앙값(arr):
    index = int((len(arr)-1)/2)
    return arr[index]

def 최빈값(arr):
    tmp = Counter(arr).most_common()
    if len(tmp)==1 :
        return tmp[0][0]
    elif tmp[0][1] == tmp[1][1] :
        return tmp[1][0]
    else : return tmp[0][0]

def 범위(arr) :
    return abs(max(arr)-min(arr))

def 산술평균(arr) : 
    return int(round(sum(arr)/len(arr),0))

print(산술평균(arr))
print(중앙값(arr))
print(최빈값(arr))
print(범위(arr))
