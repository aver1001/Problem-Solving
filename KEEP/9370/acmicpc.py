import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split(' '))
    s, g, h = map(int, sys.stdin.readline().rstrip().split(' '))

    table = {}
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split(' '))

        if a in table:
            table[a][b] = d
        else:
            table[a] = {b: d}

        if b in table:
            table[b][a] = d
        else:
            table[b] = {a: d}

    target = set()
    for _ in range(t):
        target.add(int(sys.stdin.readline().rstrip()))

print(table)
