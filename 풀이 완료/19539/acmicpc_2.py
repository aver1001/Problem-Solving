from audioop import reverse
import sys
from collections import deque
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
board = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# +1 +2 하거나
# +3 해서 다 없에야함.

# 3의 배수면 다 지울 수 있음.
# 다 3의 배수로 만들어 버릴까?
zero = []
one = []
two = []

# 나머지 기준으로 나눠준다
while board:
    tree = board.pop()

    temp = tree % 3

    if temp == 0:
        zero.append(tree)
    elif temp == 1:
        one.append(tree)
    elif temp == 2:
        two.append(tree)


while True:

    # 나머지 1 그룹이 존재한다면
    if one:
        one.pop()
        # 나머지 2 그룹이 있다면
        if two:
            # 둘다 제거하고 끝
            two.pop()
            continue
        # 나머지 2 그룹이 없다면 0 그룹을 건들여야함
        else:
            # 0 그룹이 있다면
            if zero:
                # 제거하고 나머지 2 그룹으로 옮겨줌
                two.append(zero.pop())
                continue
            # 0 그룹이 없다면
            else:
                # 1 그룹이라도 건들여야함
                if one:
                    temp = one.pop()
                    if temp >= 4:
                        two.append(temp)
                        continue
                    else:
                        print('NO')
                        exit()
                else:
                    print('NO')
                    exit()
    # 나머지 2 그룹이 존재한다면
    if two:
        Two = two.pop()
        # 나머지 1 그룹이 존재한다면
        if one:
            # 제거 후 삭제
            One = one.pop()
            continue
        # 없다면 부득이하게 0 그룹 건들여야함
        else:
            # 잇다면 제거 후 1 그룹에 넣어줌
            if zero:
                one.append(zero.pop())
            # 없으면 만들 수 없음
            else:
                # 2그룹이라도 건들여야함
                if two:
                    temp = two.pop()
                    one.append(temp)
                    continue
                else:
                    print('NO')
                    exit()

    # 둘다 존재 안하면 성공임
    print('YES')
    exit()
