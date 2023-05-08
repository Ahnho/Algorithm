num_case = int(input())

for _ in range(num_case):
    n = int(input())

    li = []
    for _ in range(n):
        li.append(input())
    count = 0

    for log in li:
        l = log.split(" ")
        if len(log) > 100:
            count += 1
            continue
        elif len(l) != 12:
            count += 1
            continue

        elif l[1] != ':' or l[4] != ':' or l[7] != ':' or l[10] != ':':
            count += 1
            continue

        elif l[0] != 'line_name' or l[3] != 'product_name' or l[6] != 'error_level' or l[9] != 'message':
            count += 1
            continue

        elif not l[2].isalpha() or not l[5].isalpha() or not l[8].isalpha() or not l[11].isalpha():
            count += 1

    print(count)