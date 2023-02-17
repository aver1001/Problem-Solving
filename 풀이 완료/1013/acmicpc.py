import sys
import re
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())
find = re.compile('(100+1+|01)+')

for _ in range (T):
    signal = input()
    if find.fullmatch(signal) != None:
        print('YES')
    else:
        print('NO')