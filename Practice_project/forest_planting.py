def simulate(trees,soil,n):
    save = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if trees[i][j] :
                trees[i][j].sort()
                new_tree = []
                for age in trees[i][j]:
                    if age <= soil[i][j]:
                        new_tree.append(age + 1)
                        soil[i][j] -= age
                    else:
                        save[i][j] += age//2
                trees[i][j] = new_tree

    for i in range(n):
        for j in range(n):
            if save[i][j]:
                soil[i][j] += save[i][j]

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                            nx, ny = j+dx, i+dy
                            if 0 <= nx < n and 0 <= ny < n:
                                trees[ny][nx].append(1)
    return trees,soil

def heal(soil,n,k):
    for i in range(n):
        for j in range(n):
            soil[i][j] += k

def main():
    t = int(input())
    for _ in range(t):
        n, c, k, p = map(int, input().split())
        soil = []
        trees = [[[] for _ in range(n)] for _ in range(n)]

        for _ in range(n):
            soil.append(list(map(int, input().split())))
        for _ in range(c):
            x, y, age = map(int, input().split())
            trees[x][y].append(age)

        for _ in range(p):
            trees,soil = simulate(trees,soil,n)
            heal(soil,n,k)
        exict_tree = 0
        for i in range(n):
            for j in range(n):
                if trees[i][j]:
                    exict_tree += len(trees[i][j])
        print(exict_tree)

if __name__== "__main__":
    main()
