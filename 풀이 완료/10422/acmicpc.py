import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

def solution(num):
    if num % 2 == 0:
        return 0


for _ in range (N):
    num = int(sys.stdin.readline().rstrip())
    print(solution(num))

