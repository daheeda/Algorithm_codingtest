def solution(board):
    if sum(board[i][j] for i in range(len(board)) for j in range(len(board[0]))) == 0 : return 0
    else : 
        answer = 1

        for y in range(len(board)-1):
            for x in range(len(board[0])-1):
                if board[y+1][x+1] == 1 :
                    if (board[y][x]>0)&(board[y][x+1]>0)&(board[y+1][x]>0):
                        board[y+1][x+1] = min(board[y][x],board[y][x+1],board[y+1][x])+1
                        if answer < board[y+1][x+1]*board[y+1][x+1] :
                            answer = board[y+1][x+1]*board[y+1][x+1]
        return answer
