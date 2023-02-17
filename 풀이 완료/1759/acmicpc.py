from itertools import combinations
import sys
sys.stdin = open('input.txt', "r")

L, C = map(int, sys.stdin.readline().rstrip().split(' '))
commend = sys.stdin.readline().rstrip().split(' ')

commend.sort()
for com in combinations(commend, L):
    mo = 0
    za = 0
    for i in com:
        if i in {'a', 'e', 'i', 'o', 'u'}:
            mo += 1
        else:
            za += 1

    if mo >= 1 and za >= 2:
        print(''.join(com))
