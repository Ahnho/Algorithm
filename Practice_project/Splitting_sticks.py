n = int(input())

for _ in range(n):
    lin = input()
    stack = []
    bars = 0
    for i in range(len(lin)):
        if lin[i] == '(' and lin[i+1] == '(':
            stack.append(0)
        elif lin[i] == ')' and lin[i-1] == ')':
            bars += stack.pop() + 1
        elif lin[i] == '(' and lin[i+1] == ')':
            for j in range(len(stack)):
                stack[j] += 1

    print(bars)
     
