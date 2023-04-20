def solution(nums):
    uniq = len(set(nums))
    if int(len(nums)/2) >= uniq :
        return uniq
    else : 
        return int(len(nums)/2)
