def solution(board, moves):
    answer = 0
    stack=[-1]
    size = len(board)
    
    for i in range(0,len(moves)):
        move = moves[i]
        for j in range(0,size):
            if board[j][move-1] != 0:
                if stack[-1] == board[j][move-1] :
                    stack.pop()
                    answer += 2
                    board[j][move-1]=0
                    break
                else :
                    stack.append(board[j][move-1])
                    board[j][move-1]=0
                    break
    
    return answer
