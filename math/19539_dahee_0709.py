N = int(input()) # <- 엄청 큼..
h = input().split(" ") # 원하는 나무 상태
h = list(map(int,h))

def make_tree(current):
    
    count_even = 0
    count_odd = 0
    
    for i in range(0, len(current)):
        if (current[i]%2 == 0):
            count_even += current[i]/2
        if (current[i]%2 == 1):
            count_even += (current[i]-1)/2
            count_odd +=1
            current[i] = current[i]-1
    
    if (count_even < count_odd) : print("NO")
    else : 
        if (sum(current)-(count_odd)*2)%3 == 0 : print("YES")
        else : print("NO")
            
make_tree(h)
