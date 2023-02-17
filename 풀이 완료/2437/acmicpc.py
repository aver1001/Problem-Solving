import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# 일단 경우의수 구해보고 최적화를 해보자.
# 작은거부터 더해가면서 중간에 비는거 리턴?
commend.sort()

Max = 1
for num in commend:
    if Max < num:
        break

    Max += num
print(Max)
