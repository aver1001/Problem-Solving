import sys
sys.stdin = open('input.txt', "r")

N, S = map(int, sys.stdin.readline().rstrip().split(' '))
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

lt, rt = 0, 0
hap = commend[0]
answer = 100000
while True:

    if hap < S:
        rt += 1
        if rt >= N:
            break
        hap += commend[rt]

    else:
        answer = min(answer, rt-lt+1)
        hap -= commend[lt]

        lt += 1


if answer == 100000:
    print(0)
else:
    print(answer)
