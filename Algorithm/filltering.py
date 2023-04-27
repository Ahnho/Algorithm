import re

# def fullmatch(pattern, string):
#     if len(pattern) != len(string):
#         return False

#     for i in range(len(pattern)):
#         if pattern[i] != string[i]:
#             return False

#     return True

def pr(answer):
    an = ''
    for a in answer:
        an += a + " "

    return an[:-1]

num_case = int(input())            

for _ in range(num_case):
    n, m = map(int, input().split())
    li = list(input().split())
    words = input().split()
    answer = []

    for i in range(len(words)):
        word = words[i]
        regular = word.replace('.', '[a-z]{1,%d}' % m)
        # print(regular)
        p = 0

        for j in li:
            if re.fullmatch(regular, j):
            # if fullmatch(regular, j):
                answer.append('#' * len(word))
                p = 1
                break
        if p == 0:
            answer.append(word)

    print(pr(answer))
