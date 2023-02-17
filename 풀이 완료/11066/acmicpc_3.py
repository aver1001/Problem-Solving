import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())


def printBoard():
    for i in DP:
        print(i)
    print()


for _ in range(T):

    N = int(sys.stdin.readline().rstrip())
    fileList = [0] + list(map(int, sys.stdin.readline().rstrip().split(' ')))
    '''
    A+B 두개로 나눈뒤 두개의 최솟값?
    2차원 배열 만든뒤 A~B까지의 최솟값 으로 DP 계산해보는건 어떨까
    '''

    DP = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if j == i+1:
                DP[i][j] = fileList[i] + fileList[j]

    for i in range(N-1, 0, -1):
        for j in range(1, N+1):
            if DP[i][j] == 0 and j > i:
                DP[i][j] = min([DP[i][k]+DP[k+1][j]
                               for k in range(i, j)]) + sum(fileList[i:j+1])

    print(DP[1][-1])


'''
0 1  1 2  2 3  3 4
0      2
     1      3
          2      4
0           3
     1           4
0                4
'''
