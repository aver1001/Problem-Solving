from collections import deque
import sys
sys.stdin = open('input.txt', "r")

N, L = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque()
d_list = [0] * N
for i in range(N):
    left = i - L + 1  # 범위의 시작 값

    while queue:  # front에 존재하는 최솟값이 범위 안의 녀석일 때까지
        if queue[0][1] < left:
            queue.popleft()
        else:
            break

    while queue:  # 자신보다 작은 녀석이 나올 때까지
        if queue[-1][0] > num_list[i]:
            queue.pop()
        else:
            break

    # (값, 인덱스) 삽입
    queue.append((num_list[i], i))
    d_list[i] = queue[0][0]

print(*d_list)
