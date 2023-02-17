import sys
from tkinter import E
sys.stdin = open('input.txt', "r")

target = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
word = set()
dp = [0]*(len(target) + 1)
Maximum = 0
Minimum = 101
for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    Maximum = max(Maximum, len(temp))
    Minimum = min(Minimum, len(temp))
    word.add(temp)

targetN = len(target)
lt, rt = 0, 0


def solution(lt, rt):

    while rt < targetN+1:
        if target[lt:rt] in word:
            dp[rt] = 1
        rt += 1

    for i in range(targetN+1):
        if dp[i] == 1:
            lt, rt = i, i

            while rt < targetN+1:
                if target[lt:rt] in word:
                    dp[rt] = 1
                rt += 1


solution(0, 0)
print(dp[-1])
