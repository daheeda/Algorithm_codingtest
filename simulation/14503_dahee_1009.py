n,m = map(int,input().split())
sr,sc,sd = map(int,input().split())
place = [list(map(int,input().split())) for _ in range(n)]
place = [[1]*m] + place + [[1]*m]
place = [ [1]+i+[1] for i in place ]

def move(arr,x,y,d,cnt):

    dd = {0:[y-1,x], 1:[y,x+1], 2:[y+1,x], 3:[y,x-1]}
    
    if arr[y][x] == 0 : 
        arr[y][x] = 2 
        cnt += 1
        
    if (arr[y+1][x]*arr[y][x+1]*arr[y-1][x]*arr[y][x-1]) != 0 :
        back = {0:[y+1,x], 1:[y,x-1], 2:[y-1,x], 3:[y,x+1]}
        if arr[back[d][0]][back[d][1]] == 2 :
            return move(arr,back[d][1],back[d][0],d,cnt)
        else : return cnt
    else :
        while True :
            d = (d+1)%4
            d = (d+1)%4
            d = (d+1)%4
            if arr[dd[d][0]][dd[d][1]] == 0:
                return move(arr,dd[d][1],dd[d][0],d,cnt)
        
rr = move(place, sc+1, sr+1, sd, 0)
print(rr)
