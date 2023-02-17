import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline().rstrip())
commend = set(map(int, sys.stdin.readline().rstrip().split(' ')))

temp = []
for c in commend:

    firstC = c
    hap = 0

    while True:
        if c % 3 == 0:
            c = c // 3
            hap -= 1
        elif c % 2 == 0:
            c = c // 2
            hap += 1
        else:
            break

    temp.append([firstC, hap])

temp.sort(key=lambda x: x[1])
for x, y, in temp:
    print(x, end=' ')
