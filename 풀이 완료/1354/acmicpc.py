import sys
sys.stdin = open('input.txt', "r")

# Ai = 1 (i ≤ 0)
# Ai = A⌊i/P⌋-X + A⌊i/Q⌋-Y (i ≥ 1)

check = {}

N, P, Q, X, Y = map(int, sys.stdin.readline().rstrip().split())


def solution(i :int):
    if i <= 0:
        return 1
    check[i] = solution(i//P-X) + solution(i//Q-Y)
    return check[i]

print(solution(N))