import sys
from collections import deque
sys.stdin = open('input.txt', "r")

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

isRight = True

# A를 지울수있는대까지 지운다
# B지우고 뒤집는다


while True:

    if len(A) == len(B):
        break

    if B[-1] == 'A':
        B = B[:-1]

    elif B[-1] == 'B':
        B = B[:-1]
        B = B[::-1]


if A == B:
    print(1)
else:
    print(0)
