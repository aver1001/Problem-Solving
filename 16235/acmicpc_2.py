from collections import deque
import sys
sys.stdin = open('input.txt', "r")
'''
봄
나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
만약 땅에 양분이 부족할시 즉시 죽는다

여름
봄에 죽은 나무가 양분으로 변한다
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점은 버린다

가을 
나무가 번식한다
나무의 나이가 5의 배수이면 인접한 8칸에 나무가 생긴다
땅을 벗어나는 칸에는 나무가 생기지 않는다

겨울
S2D2 땅을 돌아다니며 양분을 추가한다
각 칸에 추가되는 양분의 양은 A[r][c] 이다
'''


N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))


def Spring():
    '''
    봄
        나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다
        하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
        만약 땅에 양분이 부족할시 즉시 죽는다
    '''
    newTree = []
    for y in range(N):
        for x in range(N):
            temp = []
            while treeInfo[y][x][1]:
                # 양분을 먹을 수 있다면
                if treeInfo[y][x][0] - treeInfo[y][x][1][-1] >= 0:
                    treeYear = treeInfo[y][x][1].pop()
                    temp.append(treeYear+1)
                    # 양분 제거해준다
                    treeInfo[y][x][0] -= treeYear
                    # 가을에 번식용으로 체크
                    if (treeYear+1) % 5 == 0:
                        newTree.append([y, x])
                else:
                    break
            # 죽은 나무들 양분으로 변경해준다
            Summer(y, x)
            treeInfo[y][x][1] = temp
            treeInfo[y][x][1].sort(reverse=True)
    # 가을에 번식해주고
    Fall(newTree)
    # 겨울에 S2D2가 열일한다
    Winter()


def Summer(y, x):
    '''
    여름
        봄에 죽은 나무가 양분으로 변한다
        각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점은 버린다
    '''
    for treeYear in treeInfo[y][x][1]:
        treeInfo[y][x][0] += treeYear//2


def Fall(newTree):
    '''
    가을 
        나무가 번식한다
        나무의 나이가 5의 배수이면 인접한 8칸에 나무가 생긴다
        땅을 벗어나는 칸에는 나무가 생기지 않는다
    '''
    for y, x in newTree:
        for dy, dx in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            ty = dy+y
            tx = dx+x
            if 0 <= tx < N and 0 <= ty < N:
                treeInfo[ty][tx][1].append(1)


def Winter():
    for y in range(N):
        for x in range(N):
            treeInfo[y][x][0] += A[y][x]


def printBoard():
    for i in treeInfo:
        print(i)
    print()


def surviveTree():
    answer = 0
    for y in range(N):
        for x in range(N):
            answer += len(treeInfo[y][x][1])
    print(answer)
# 3차원 배열을 만들어서 처리하자
# [[양분의 수],[나무들의 나이],[죽은나무 나이]]


# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
treeInfo = [[[5, [], []] for _ in range(N)]for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().rstrip().split(' '))
    x -= 1
    y -= 1
    treeInfo[x][y][1].append(z)

for y in range(N):
    for x in range(N):
        treeInfo[y][x][1].sort()


for _ in range(K):
    Spring()
surviveTree()
