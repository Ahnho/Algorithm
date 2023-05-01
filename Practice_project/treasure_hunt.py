n_case = int(input())

def rule(a,b):
    if a == "F":
        if b == "F":
            return "F"
        elif b == "R":
            return "R"
        elif b == "L":
            return "L"
        elif b == "B":
            return "B"
    elif a == "R":
        if b == "F":
            return "R"
        elif b == "R":
            return "B"
        elif b == "L":
            return "F"
        elif b == "B":
            return "L"
    elif a == "L":
        if b == "F":
            return "L"
        elif b == "R":
            return "F"
        elif b == "L":
            return "B"
        elif b == "B":
            return "R"
    elif a == "B":
        if b == "F":
            return "B"
        elif b == "R":
            return "L"
        elif b == "L":
            return "R"
        elif b == "B":
            return "F"

keys = {'F' : 0, 'R' : 1, 'L' : 2, 'B' : 3}

for _ in range(n_case):
    n = int(input())
    map = [list(input().split()) for _ in range(n)]
    li = [[[0] * 4 for i in range(n)] for j in range(n)]
    li[0][0][3] = 1
    r,c = 0,0 
    before = "B"
    while 1 : 
        now = map[r][c]
        ro = rule(before, now[0])
        if ro == "F":
            r = r+int(now[1])
            before = ro

        elif ro == "B":
            r = r-int(now[1])
            before = ro

        elif ro == "R":
            c = c+int(now[1])
            before = ro

        elif ro == "L":
            c = c-int(now[1])
            before = ro
        li[r][c][keys[before]] += 1
        if li[r][c][keys[before]] > 1:
            print(r,c)
            break
