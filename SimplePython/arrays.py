def tribonacci(signature, n):
    end = 3
    start = 0
    tlist = signature
    while len(tlist) < n:
        summ = 0
        for i in range(start, end):
            summ += tlist[i]

        start += 1
        end += 1

        tlist.append(summ)
        sum

    return tlist

print(tribonacci([1, 1, 1], 10))