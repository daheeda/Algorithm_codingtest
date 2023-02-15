s = input()
res = []
for i in range(0,len(s)) : 
    for j in range(i+1,len(s)+1):
        res.append(s[i:j])
              
print(len(set(res)))
