import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', "r")
'''
IC = 차이가 2 이하일때만 정확한 비교를 해줌

더블 라운드 로빈

매 라운드마다 각 원소들이 자기 이외의 모든 원소들과 비교
R1 = 다른 원소들이랑 비교해서 자신이 더 큰 갯수
d(k) = |r1(k) + r2(k)|


0 = (2-2 ,1-1, 0-0)
1 = (2-1, 1-0,1-2,0-1)
2 = (2-0, 0-2)

결국 이기거나 지거나 둘중 하나

이기는경우 지는경우의 조합으로 다음걸 갈 수 있음.

'''

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))


def DFS(idx, beforestate):

    if idx == N:
        return True

    if beforestate == 'win':
        if commend[idx] == 2+idx:
            return False

    elif beforestate == 'lose':
        if commend[idx] == 0+idx:
            return False

    if DFS(idx+1, 'lose') or DFS(idx+1, 'win'):
        return True


if commend[0] == 0:
    #승리 - 승리
    #패배 - 패배

    if DFS(1, 'win') or DFS(1, 'lose'):
        print('YES')
    else:
        print('NO')


elif commend[0] == 1:
    # 승리 - 패배
    # 패배 - 승리
    if DFS(1, 'win') and DFS(1, 'lose'):
        print('YES')
    else:
        print('NO')


# 앞에서 이겼다면 나는 2 불가능
# 앞에서 졌다면 나는 0 불가능
