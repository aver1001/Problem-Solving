import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())


def isSame(lt, rt, cnt):

    while True:
        if lt > rt:
            if cnt == 1:
                return 1
            else:
                return 0

        if s[lt] != s[rt]:
            if cnt == 0:
                temp = isSame(lt+1, rt, cnt+1)
                temp = min(temp, isSame(lt, rt-1, cnt+1))
                return temp
            if cnt == 1:
                return 2
        lt += 1
        rt -= 1


for _ in range(N):
    s = sys.stdin.readline().rstrip()

    sN = len(s)
    lt = 0
    rt = sN-1
    print(isSame(0, rt, 0))
