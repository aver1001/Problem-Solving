import sys
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
meat = []
for _ in range(N):
    weight, price = map(int, sys.stdin.readline().rstrip().split(' '))
    meat.append([weight, price])

# 가격이 싼 순서, 무거운 순서 대로 정렬한뒤
meat.sort(key=lambda x: (x[1], -x[0]))
hap = 0
answer = 2_147_483_648
priceH = 0
for i in range(N):
    weight, price = meat[i]
    hap += weight
    # 가격이 다를경우 가격 초기화
    if i != 0 and price == meat[i-1][1]:
        priceH += price
    # 가격이 같을경우 가격 더해주기
    else:
        priceH = price

    if hap >= M:
        answer = min(answer, priceH)

        if hap == price:
            break

    before = price

if answer == 2_147_483_648:
    print(-1)
else:
    print(answer)
