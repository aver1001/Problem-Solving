import re
import sys
from collections import deque
sys.stdin = open('input.txt', "r")

A, B, C = map(int, sys.stdin.readline().rstrip().split())

'''
A,B는 비어있고 C는 가득 차있는 상태로 시작한다.
어떤 물통에 있는 물을 다른 물통으로 쏟아 부을 수 있다.
이때 한 물통이 비거나, 가득찰때까지 물을 부을 수 있다.
if A == 0 일떄 C 에 담겨 있을 수 있는 물의 양을 모두 구해서 오름차순으로 정렬해라
'''

# DP?
# A, B 에 들어있는 물의 양을  DP Table로 설정해서 해결하자
DP = [[False]*201 for _ in range(201)]

queue = deque([[0, 0, C]])
result = set()


def moveWater(a, aMax, b):
    # b => a

    # a + b 가 aMax 넘을경우
    if a+b > aMax:
        return aMax, a+b-aMax

    # a+ b 가 aMax 같거나 작을경우
    elif a+b <= aMax:
        return a+b, 0


while queue:
    a, b, c = queue.popleft()

    '''
    가능한 경우의 수
    a => b
    a => c
    b => a
    b => c
    c => a
    c => b
    '''

    # a => b
    tempB, tempA = moveWater(b, B, a)
    if DP[tempA][tempB] == False:
        DP[tempA][tempB] = True
        queue.append([tempA, tempB, c])
        if tempA == 0:
            result.add(c)

    # a => c
    tempC, tempA = moveWater(c, C, a)
    if DP[tempA][b] == False:
        DP[tempA][b] = True
        queue.append([tempA, b, tempC])
        if tempA == 0:
            result.add(tempC)

    # b => a
    tempA, tempB = moveWater(a, A, b)
    if DP[tempA][tempB] == False:
        DP[tempA][tempB] = True
        queue.append([tempA, tempB, c])
        if tempA == 0:
            result.add(c)

    # b => c
    tempC, tempB = moveWater(c, C, b)
    if DP[a][tempB] == False:
        DP[a][tempB] = True
        queue.append([a, tempB, tempC])
        if a == 0:
            result.add(tempC)

    # c => a
    tempA, tempC = moveWater(a, A, c)

    if DP[tempA][b] == False:
        DP[tempA][b] = True
        queue.append([tempA, b, tempC])
        if tempA == 0:
            result.add(tempC)

    # c => b
    tempB, tempC = moveWater(b, B, c)
    if DP[a][tempB] == False:
        DP[a][tempB] = True
        queue.append([a, tempB, tempC])
        if a == 0:
            result.add(tempC)

result = list(result)
result.sort()
print(*result)
