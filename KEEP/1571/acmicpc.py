import math
import sys
sys.stdin = open('input.txt', "r")

board = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

target = sys.stdin.readline().rstrip()
print(dir(math))
gong = 1
for b in board:
    gong = math.lcm(gong, len(b))
print(gong)
