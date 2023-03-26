numCase = int(input())

for cnt in range(numCase):
    n = int(input())
    A,B = [],[]
    sa,sb = 0,0
    for _ in range(n):
        a = input()
        if a[0] == 'O':
            ord, cnt, fac = a.split()
        else:
            ord, fac = a.split()
        if ord == "ORDER":
            if fac == 'A':
                A.append(int(cnt))
                sa += int(cnt)
            elif fac == 'B':
                B.append(int(cnt))
                sb += int(cnt)
            else : 
                if sa <= sb: 
                    A.append(int(cnt)) 
                    sa += int(cnt)
                else: 
                    B.append(int(cnt))
                    sb += int(cnt)
        else:
            if fac == 'A':
                sa -= A.pop(0)
            else:
                sb -= B.pop(0)

    print(sa,sb)