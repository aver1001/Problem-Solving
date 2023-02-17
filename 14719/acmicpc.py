import sys
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split(' '))
wall = list(map(int, sys.stdin.readline().rstrip().split(' ')))


ans = 0
for i in range(1, X - 1):
    left_max = max(wall[:i])
    right_max = max(wall[i+1:])

    compare = min(left_max, right_max)

    if wall[i] < compare:
        ans += compare - wall[i]

print(ans)
