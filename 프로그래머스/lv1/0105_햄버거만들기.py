def solution(ingredient):
    stack=[]
    cnt = 0
    for i in ingredient:
        stack.append(i)
        if len(stack)>=4:
            if stack[-4:] == [1,2,3,1]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                cnt +=1
    return cnt
  # replace 보다 stack 이 빨랐다...........
