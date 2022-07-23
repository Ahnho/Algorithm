##########################################################
##                  2 x n 타일링                       ##
##########################################################

def solution(dirs):
    answer = []
    x,y = 0,0
    dr = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        nx, ny = x + dr[d][0], y + dr[d][1] 
        if -5 <= nx <=5  and -5 <= ny <=5:
            answer.append([x,y,nx,ny])
            answer.append([nx,ny,x,y])
            x,y = nx,ny
    answer = set(map(tuple,answer)) 
    return len(answer) / 2
