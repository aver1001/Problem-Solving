import sys
sys.stdin = open('input.txt', "r")

table = [[0]*31 for _ in range(31)]

for w in range(31):
    for h in range(31):
        if w >= h:
            if h == 0:
                table[w][h] = 1
            else:
                table[w][h] = table[w-1][h] + table[w][h-1]


while True:
    N = int(sys.stdin.readline().rstrip())

    if N == 0:
        break

    print(table[N][N])
