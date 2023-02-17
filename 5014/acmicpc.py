import sys
from collections import deque
sys.stdin = open('input.txt', "r")
'''
총 F층으로 이루어진 고층 건물에 사무실이 있고,
회사가 있는 곳의 위치는 G 층 입니다.
강호가 지금 있는곳은 S층이고 엘레베이터를 타고 G층으로 이동하려고 합니다.

U 버튼과 D 버튼만을 사용해서 회사 사무실로 도착하세요
최소값을 리턴하고, 이동할수 없을때는 "use the staris" 를 출력하세요
출발은 1층에서 합니다.
'''

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split(' '))
commend = sys.stdin.readline().rstrip().split(' ')

INF = sys.maxsize
check = [False]*(F+20)
check[0] = 0
# [내위치, 버튼누른 횟수]
queue = deque([[S, 0]])

while queue:
    now, cnt = queue.popleft()

    # 도착했을경우
    if now == G:
        print(cnt)
        exit()
        break

    for add in [U, -D]:
        next = now+add
        # 건물을 벗어나지 않고, 다음 갈 곳이 내가 최솟값일경우
        if 1 <= next <= F and check[next] == False:
            # 최솟값 업데이트
            check[next] = True
            # 큐에 추가
            queue.append([next, cnt+1])
print('use the stairs')
