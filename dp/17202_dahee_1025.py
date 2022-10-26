ph1=list(map(int,input()))
ph2=list(map(int,input()))
res=[]
for i in range(0,8):
    res.append(ph1[i])
    res.append(ph2[i])
while len(res) > 2 :
    tmp=[]
    for i in range(0,len(res)-1,1):
        tmp.append((res[i]+res[i+1])%10)
    res=tmp
print(str(res[0])+str(res[1]))
