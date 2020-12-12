def solution(board, moves):
    case = [0]
    for i in range(len(moves)):
        a = 0
        while 1:
            if a == len(board):
                break
            if board[a][moves[i] - 1] != 0 :
                case.append(board[a][moves[i] - 1])
                board[a][moves[i] - 1] = 0
                break 
            a += 1
        if len(case) >= 2 :
            if case[len(case)-1] == case[len(case)-2]:
                case.pop()
                case.pop()

        
    return len(case)