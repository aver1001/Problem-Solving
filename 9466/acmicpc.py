import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    N = int(sys.stdin.readline().rstrip())
    commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    check = [False] * (N+1)
    table = {i: commend[i-1] for i in range(1, N+1)}
    answer = 0
    for i in range(1, N+1):

        # 확인 안된 친구
        if check[i] == False:

            queue = deque([i])
            before = set()
            while queue:
                Loc = queue.popleft()

                if Loc in before:
                    beforeLoc = Loc
                    while True:
                        answer += 1
                        nowLoc = table[beforeLoc]
                        if nowLoc == Loc:
                            break
                        beforeLoc = nowLoc
                    break

                if check[Loc] == True:
                    break
                check[Loc] = True
                queue.append(table[Loc])
                before.add(Loc)
    print(N-answer)
