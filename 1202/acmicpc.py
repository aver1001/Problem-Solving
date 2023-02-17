import sys
import heapq
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split(' '))

jewel = []
for _ in range(N):
    # 무개 가격
    weight, cost = map(int, sys.stdin.readline().rstrip().split(' '))
    jewel.append([weight, cost])
jewel.sort(reverse=True)
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline().rstrip()))
bags.sort(reverse=True)
# 결국 가장 작은 무게에서
# 가장 가져갈 수 있는 높은 금액을 찾아서 가져가야함.

answer = 0
waitting = []
while bags:
    nowWeight = bags.pop()

    while jewel:
        weight, cost = jewel.pop()
        if weight > nowWeight:
            jewel.append([weight, cost])
            break
        else:
            heapq.heappush(waitting, [-cost, weight])
    if waitting:
        cost, weight = heapq.heappop(waitting)
        answer += -cost

print(answer)
