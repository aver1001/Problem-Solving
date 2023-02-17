import sys
import heapq
sys.stdin = open('input.txt', "r")

info = dict()
answer = 0
Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    q = sys.stdin.readline().rstrip().split(' ')

    if q[0] == '1':
        name = q[1]
        cost = q[3:]
        if name in info:
            for c in cost:
                heapq.heappush(info[name], -int(c))
        else:
            temp = []
            for i in cost:
                temp.append(-int(i))
            heapq.heapify(temp)
            info[name] = temp

    elif q[0] == '2':
        name = q[1]
        cnt = int(q[2])

        if name in info:
            while info[name]:
                answer += heapq.heappop(info[name])
                cnt -= 1

                if cnt == 0:
                    break


print(-answer)
