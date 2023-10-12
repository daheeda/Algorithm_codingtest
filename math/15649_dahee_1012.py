from itertools import permutations

n,m = map(int,input().split())

arr = [ i for i in range(1,n+1)]

for i in list(permutations(arr,m)):
    i = list(map(str,i))
    print(' '.join(i))
    
