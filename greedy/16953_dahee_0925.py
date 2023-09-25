a,b = map(int,input().split())
tree = [[a]]

for i in range(int(b/2)+1):
    tmp = []
    for j in range(len(tree[i])):
        if int(str(tree[i][j])+'1') <= b :
            tmp.append(int(str(tree[i][j])+'1'))
        if tree[i][j]*2 <= b : 
            tmp.append(tree[i][j]*2)
    if b in tmp :
        print(i+2)
        break
    elif len(tmp) == 0 :
        print(-1)
        break
    else :
        tree.append(tmp)
        
