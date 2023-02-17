import sys
sys.stdin = open('input.txt', "r")

Min, Max = map(int, sys.stdin.readline().rstrip().split(' '))


table = set()

cnt = Max-Min + 1
i = 2
while True:
    if i ** 2 > Max:
        break

    start = Min // i**2

    if Min % (i**2) != 0:
        start += 1

    while start * (i**2) <= Max:
        if start * (i**2) not in table:
            table.add(start * (i**2))
            cnt -= 1
        start += 1
    i += 1


print(cnt)
