import sys
import heapq
sys.stdin = open('input.txt', "r")


'''
정렬된 두 묶음의 숫자 카드가 있다고 하자.
각각의 카드의 수를 A,B라고 할떄
최소한 몇번의 비교가 필요한지 구하는 프로그램을 작성하시오
'''

# 먼저 그룹을 지어서 더한경우 그 값이 계속해서 중복해서 더해지는 방식
# 그러므로 중복되어 더해지는 수가 작은수여야함.
# 최솟값 + 최솟값 더하는게 가장 최선의 방법이며
# 그값을 다시 넣어 촤솟값 + 최솟값 하는게 베스트로 보임
# 최솟값을 계속 꺼내야 하기때문에 힙 쓰면 될듯.
N = int(sys.stdin.readline().rstrip())
Card = []
for _ in range(N):
    Card.append(int(sys.stdin.readline().rstrip()))

heapq.heapify(Card)

answer = 0
while len(Card) != 1:
    c1 = heapq.heappop(Card)
    c2 = heapq.heappop(Card)

    temp = c1 + c2
    answer += temp
    heapq.heappush(Card, temp)
print(answer)
