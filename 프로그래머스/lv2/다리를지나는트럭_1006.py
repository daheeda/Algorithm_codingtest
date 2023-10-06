from collections import deque

def solution(bridge_length, weight, truck_weights):
    ing = deque([])
    res = 0
    truck_weights = deque(truck_weights)
    left_time = deque([])
    while (len(truck_weights) > 0):
        print(ing,res,left_time)
        if left_time.count(0) > 0 :
            ing.popleft()
            left_time.popleft()
        if (sum(ing) + truck_weights[0] <= weight) & (len(ing) < bridge_length): # 개수 가능 무게 가능
                truck_in = truck_weights.popleft()
                left_time = deque([ i-1 for i in left_time])
                res += 1
                ing.append(truck_in)
                left_time.append(bridge_length)
        else : # 불가능 => 제거
                add = left_time.popleft()
                ing.popleft()
                left_time = deque([ i-add for i in left_time])
                res += add
                if (sum(ing) + truck_weights[0] <= weight):
                    truck_in = truck_weights.popleft()
                    ing.append(truck_in)
                    left_time.append(bridge_length)
    print(ing,res,left_time)
    return res+left_time[-1]
