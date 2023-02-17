import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
S = 0

for _ in range(N):
    temp = sys.stdin.readline().rstrip().split(' ')

    if temp[0] == 'add':
        # S에 x를 추가한다. 이미 있는경우에는 연산을 무시한다.
        S = S | (1 << int(temp[1]))

    elif temp[0] == 'remove':
        # S에 x를 제거한다. 이미 없는 경우에는 연산을 무시한다.
        S = S & ~(1 << int(temp[1]))

    elif temp[0] == 'check':
        # S에 x가 있으면 1을, 없으면 0을 출력한다.
        if S & (1 << int(temp[1])):
            print(1)
        else:
            print(0)

    elif temp[0] == 'toggle':
        # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
        # XOR == 다르면 1 반환
        S = S ^ (1 << int(temp[1]))
    elif temp[0] == 'all':
        # S를 {1, 2, ..., 20} 으로 바꾼다.
        S = 1 << 21 - 1
    elif temp[0] == 'empty':
        # S를 공집합으로 바꾼다.
        S = 0
