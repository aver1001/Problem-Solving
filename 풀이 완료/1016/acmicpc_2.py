import sys
from math import sqrt
sys.stdin = open('input.txt', "r")

Min, Max = map(int, sys.stdin.readline().rstrip().split(' '))


table = set()

cnt = 0
if Min == 1:
    Min = 2
    cnt += 1
for idx in range(Min, Max+1):

    if sqrt(idx) % 1 == 0 and (idx not in table):
        cnt += 1
        temp = idx*idx
        while True:
            if temp > Max + 1:
                break

            table.add(temp)
            temp = temp+idx

print(cnt)
