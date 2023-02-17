import sys
sys.stdin = open('input.txt', "r")

M, N = map(int, sys.stdin.readline().rstrip().split(' '))
commend = []
for _ in range(N):
    commend.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

grow = [1]*(2*M-1)


def afterDay(commend):
    '''
    제일 왼쪽 열과, 제일 위쪽 행의 애벌레들은 자신이 자라는 정도를 스스로 결정한다. 
    이들은 입력으로 주어질 것이다. 
    애벌레들이 자라는 정도를 왼쪽 제일 아래 칸에서 시작하여 위쪽으로 가면서 읽고,
    제일 위쪽 칸에 도착하면 오른쪽으로 가면서 행의 끝까지 읽었다고 하자. 
    모든 입력에서 이렇게 읽은 값들은 감소하지 않는 형태이다.
    '''
    y = M-1
    x = 0
    pt = 0
    cnt = 0
    while x != M:

        while pt != 2:
            if commend[pt] == 0:
                pt += 1
            else:
                break

        grow[cnt] += pt
        cnt += 1
        if y != 0:
            y -= 1
        else:
            x += 1

        commend[pt] -= 1


for c in commend:
    afterDay(c)
temp = grow[:M]

for idx in range(M-1, -1, -1):
    print(grow[idx], * grow[M:])
