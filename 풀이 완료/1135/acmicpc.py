import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

table = {i: {'c': set(), 'm': None, 'cnt': -1} for i in range(N)}


for idx in range(1, N):
    table[idx]['m'] = commend[idx]
    table[commend[idx]]['c'].add(idx)
check = [False]*N


for idx in range(N):
    loc = idx
    while True:
        table[loc]['cnt'] += 1
        if table[loc]['m'] == None:
            break

        loc = table[loc]['m']

answer = []
queue = deque([(0, 0)])
while queue:
    loc, time = queue.popleft()
    if check[loc] != False:
        continue
    check[loc] = time
    answer.append(time)

    temp = []
    for nextLoc in table[loc]['c']:
        temp.append([table[nextLoc]['cnt'], nextLoc])
    temp.sort(reverse=True)

    # 자식개수,위치
    for _, nextLoc in temp:
        time += 1
        queue.append((nextLoc, time))

print(check)
print(max(answer))

#           0
#       0           0
#               0       0
