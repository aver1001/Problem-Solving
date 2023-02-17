import sys
sys.stdin = open('input.txt', "r")

N, A, B, C, D = map(int, sys.stdin.readline().rstrip().split())
global answer
answer = 0


def DFS(y, x, route, probability):
    global answer

    if len(route) == N+1:
        answer += probability
        return

    for dx, dy, proba in [[1, 0, A], [-1, 0, B], [0, 1, C], [0, -1, D]]:

        ty = y + dy
        tx = x + dx

        if (ty, tx) not in route:
            route.add((ty, tx))
            DFS(ty, tx, route, probability*(proba/100))
            route.remove((ty, tx))


route = {(0, 0)}
DFS(0, 0, route, 1)

print(answer)
