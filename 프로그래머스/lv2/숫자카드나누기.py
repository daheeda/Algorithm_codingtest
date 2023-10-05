def gcd(k,kk):
    if k % kk == 0 : return kk
    else: return gcd(kk,k%kk)

def solution(arrayA, arrayB):
    
    a = min(arrayA)
    b = min(arrayB)
    
    for i in range(0,len(arrayA)):
        a = gcd(arrayA[i],a)
    for i in range(0,len(arrayB)):
        b = gcd(arrayB[i],b)
    
    resb = sum([1 for x in arrayB if x%a > 0]) 
    resa = sum([1 for x in arrayA if x%b > 0])
    
    if (resb == len(arrayB)) & (resa == len(arrayA)) : return max(a,b)
    elif resb == len(arrayB) : return a
    elif resa == len(arrayA) : return b
    else : return 0
