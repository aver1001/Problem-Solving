import sys
sys.stdin = open('input.txt', "r")
N,P,Q = map(int, sys.stdin.readline().rstrip().split())
DP = {0:1}
def solution(i : int):
    if i in DP: return DP[i]
    DP[i] = solution(i//P) + solution(i//Q)
    return DP[i]

print(solution(N))