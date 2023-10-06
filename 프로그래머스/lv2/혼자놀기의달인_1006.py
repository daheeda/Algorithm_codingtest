def solution(cards):
    answer = 0
    open = [1]*len(cards)
    res = [0]
    for now in cards :
        tmp = 0
        if open[now-1] == 1 :
            while True :
                if open[now-1] == 1 :
                    open[now-1] = 0
                    now = cards[now-1]
                    tmp += 1
                else : break
        res.append(tmp)
        if sum(res) == len(cards):break
    res.sort()
    return res[-1]*res[-2]
