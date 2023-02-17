import sys
sys.stdin = open('input.txt', "r")

A,B = map(int, sys.stdin.readline().rstrip().split())
def solution(n :int) -> int:
    cnt = 1
    answer = n
    while ((1<<cnt) <= n):
        answer += n//(1<<cnt) * (1<<cnt)//2
        cnt += 1
    return answer

print(solution(B)-solution(A-1))