import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    commend = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    Array = sys.stdin.readline().rstrip()[1:-1].split(',')
    if N == 0:
        Array = []
    # print(Array)
    # 좌우 포인터를 하나씩 생성해준다.
    isOrigin = True
    Array = deque(Array)

    for c in commend:
        if c == 'R':
            isOrigin = not isOrigin
        elif c == 'D':
            if len(Array) == 0:
                print('error')
                break
            if isOrigin:
                Array.popleft()
            else:
                Array.pop()
    else:

        if len(Array) == 0:
            print('[]')
        else:
            if isOrigin:
                print("[" + ",".join(Array) + "]")

            else:
                Array.reverse()
                print("[" + ",".join(Array) + "]")


# AC는 정수 배열에 연산을 하기 위해 만든 언어
# 두가지 함수 R(뒤집기) ,D(버리기) 가 존재

# R은 배열에 있는 수를 뒤집는 함수
# D는 첫번쨰 수를 버리는 함수 =>? 0번쨰 인덱스를 말하는것?
# 배열이 비어있는데 D쓰면 에러가 발생

# 함수를 조합해서 한번에 사용함.
#

# 시간복잡도상 앞에걸 뺼수는 없음.
# 맨 뒤 뺴줘야함.

# 아니면 그냥 뺴지말고 체크만할까? 이게 더 좋아보이는 방법같음
