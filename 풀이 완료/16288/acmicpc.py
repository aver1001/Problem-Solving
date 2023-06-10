import sys
sys.stdin = open('input.txt', "r")

# N 입국 승객 수
# K 여권 심사 창구 수
N,K = map(int, sys.stdin.readline().rstrip().split())

# order 승객이 입국장을 빠져 나가는 순서
order = reversed(list(map(int, sys.stdin.readline().rstrip().split())))

#심사창구
check = [999]*K

for n in order:
    for k in range (K):
        if check[k] > n:
            check[k] = n
            break
    else:
        print('NO')
        exit(0)
print('YES')

