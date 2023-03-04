n = int(input())
arr= []
for _ in range(n):
    arr.append(list(map(int,input().split())))
nlist = [128,64,32,16,8,4,2,1]
nlist = nlist[nlist.index(n):]
wlist = [0]*len(nlist)
blist = [0]*len(nlist)
for div in nlist :  
    index = nlist.index(div)
    for x in range(int(len(arr)//div)):
        for y in range(int(len(arr)//div)):
            divarr = [row[div*x:div*x+div] for row in arr[div*y:div*y+div]]
            if sum(divarr,[]).count(0) == 0:
                wlist[index] += 1
            elif sum(divarr,[]).count(1) == 0:
                blist[index] += 1

for idx in range(len(nlist)-1,0,-1): 
    wlist[idx] = wlist[idx] - wlist[idx-1]*4
    blist[idx] = blist[idx] - blist[idx-1]*4
            
print(int(sum(blist)))
print(int(sum(wlist)))
