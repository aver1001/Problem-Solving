import sys
from itertools import permutations
sys.stdin = open('input.txt', "r")

'''

'''
N = int(sys.stdin.readline().rstrip())

Nlen = len(str(N))
Min = sys.maxsize
answer = []
for i in range(Nlen-1, Nlen+2):
    if i <= 0 or i > 10:
        continue
    for num in (permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], i)):
        temp = int(''.join(num))
        sub = abs(N-temp)
        if Min >= sub:
            if Min == sub:
                answer.append(temp)
            else:
                Min = sub
                answer = [temp]

if len(answer) == 0:
    print(9876543210)
else:
    print(min(answer))
