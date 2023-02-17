import sys
sys.stdin = open('input.txt', "r")

M, N = map(int, sys.stdin.readline().rstrip().split(' '))


check = [[1]*M for _ in range(M)]
grow_array = [0] * (2 * M - 1)


def printBoard(check):
    for i in check:
        print(i)
    print()


def around_grow(array):
    for y in range(1, M):
        for x in range(1, M):
            array[y][x] = array[0][x]


def grow(array, grow_array):  # g 배열을 활용하여 애벌래 크기 증가
    cnt = 0
    for j in range(M - 1, -1, -1):
        array[j][0] += grow_array[cnt]
        cnt += 1
    for j in range(1, M):
        array[0][j] += grow_array[cnt]
        cnt += 1

    for i in range(1, M):
        for j in range(1, M):
            array[i][j] += array[0][j] - 1


def sumArr():
    for y in range(1, M):
        for x in range(1, M):
            check[y][x] += check[0][x] - 1


for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    for i in range(a, a + b):
        grow_array[i] += 1
    for i in range(a + b, 2 * M - 1):
        grow_array[i] += 2
grow(check, grow_array)


for i in check:
    print(*i)
