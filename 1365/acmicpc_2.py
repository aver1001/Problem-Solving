import sys
from bisect import bisect_left
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for idx in range(N):
    if idx == 0:
        table = [commend[0]]
        continue

    if commend[idx] < table[-1]:
        temp = bisect_left(table, commend[idx])
        table[temp] = commend[idx]
    else:
        table.append(commend[idx])


# for idx in range(N-1, -1, -1):

#     if idx == N-1:
#         table2 = [commend[N-1]]
#         continue

#     if commend[idx] < table2[-1]:
#         temp = bisect_left(table2, commend[idx])
#         table2[temp] = commend[idx]
#     else:
#         table2.append(commend[idx])


print(N-len(table))
