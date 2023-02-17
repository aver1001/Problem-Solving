import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

command = []
for _ in range(N):
    command.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def getParents(a):
    if city[a] == a:
        return a
    p = getParents(city[a])
    city[a] = p
    return city[a]


def unionParent(a, b):
    a = getParents(a)
    b = getParents(b)
    if a > b:
        city[a] = b
    elif a < b:
        city[b] = a
    else:
        return


city = [i for i in range(N)]

for y in range(N):
    for x in range(N):
        if command[y][x] == 1:
            unionParent(y, x)

Before = None
route = list(map(int, sys.stdin.readline().rstrip().split(' ')))
start = city[route[0]]
for i in route:
    if start != i:
        print('NO')
        exit()

print('YES')
