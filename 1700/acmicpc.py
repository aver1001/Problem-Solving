from audioop import mul
from collections import deque
import sys
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))
table = {i: deque([]) for i in range(K+1)}
for idx in range(K):
    table[commend[idx]].append(idx)


def pageFault(multiTab):
    # 우리가 multiTab에 꽂혀잇는거 중에서 우선순위를 정해서 뽑아줘야함.
    # 그럼 우선순위는 어떻게 정할까..
    # 가장 뒤늦게 사용할 친구를 제거해야하지 않을까
    # 그럼 순위를 미리 적어놔야함. => table deque로 선언

    Max = 0
    target = -1
    for idx in multiTab:
        # 뒤에 사용할일이 없는 친구라면 바로 제거해준다
        if len(table[idx]) == 0:
            return idx

        if table[idx][0] > Max:
            Max = table[idx][0]
            target = idx

    return target


def solution():
    multiTab = set()
    answer = 0
    for idx in range(K):

        # 초반에 멀티텝 꽂아주기
        if len(multiTab) < N:
            multiTab.add(commend[idx])
            table[commend[idx]].popleft()
            continue

        # pageHit
        if commend[idx] in multiTab:
            table[commend[idx]].popleft()
            continue
        # pageFault
        else:
            target = pageFault(multiTab)
            if target == -1:
                multiTab.add(commend[idx])
            else:
                multiTab.remove(target)
                multiTab.add(commend[idx])
            table[commend[idx]].popleft()
            answer += 1
            continue

    print(answer)


solution()
