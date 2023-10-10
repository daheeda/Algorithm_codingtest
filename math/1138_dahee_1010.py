n = int(input())
people = list(map(int,input().split()))
res = []

for i in range(len(people)-1,-1,-1):
    if len(res) < people[i] :
        res.append(str(i+1))
    else :
        res.insert(people[i],str(i+1))
print(' '.join(res))
