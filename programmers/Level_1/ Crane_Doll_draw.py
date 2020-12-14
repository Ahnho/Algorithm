###########################################
##           크레인 인형 뽑기              ##
###########################################

def solution(board, moves):
    baseket = [0]
    cnt = 0 
    for i in range(len(moves)):
        a = 0
        while 1:
            if a == len(board):
                break
            if board[a][moves[i] - 1] != 0 :
                baseket.append(board[a][moves[i] - 1])
                board[a][moves[i] - 1] = 0
                break 
            a += 1
        if len(baseket) >= 2 :
            if baseket[len(baseket)-1] == baseket[len(baseket)-2]:
                baseket.pop()
                baseket.pop()
                cnt += 2

        
    return cnt