# B 뒤로가기를 실행한다.

# F 앞으로가기를 실행한다.

# A i  i번 웹사이트에 접속한다.

# C 압축을 실행한다.

import sys
sys.stdin = open('input.txt', "r")


def Back(backStack, frontStack, now):
    # 뒤로가기 공간에 1개 이상의 페이지가 저장되어 있을 때만 2,3번 과정이 실행된다, 0개일때 이 작업은 무시한다.
    # 현재 보고 있던 웹페이지를 앞으로 가기 공간에 저장한다.
    # 뒤로 가기 공간에서 방문한지 가장 최근의 페이지에 접속한다. 그리고 해당 페이지는 뒤로가기에서 삭제된다.

    # 1개 이상에 페이지가 저장되어 있을때만 실행한다.
    if len(backStack) >= 1:
        # 현재 보고 있던 웹페이지를 앞으로 가기 공간에 저장한다.
        frontStack.append(now)
        # 뒤로가기 공간에서 방문한지 가장 최근의 페이지에 접속한다.
        now = backStack.pop()
        # 그리고 해당 페이지는 뒤로가기에서 삭제된다.

    return now


def Front(backStack, frontStack, now):
    # 앞으로 가기 공간에 1개 이상의 페이지가 저장되어 있을 때만 2,3번 과정이 실행된다, 0개일때 이 작업은 무시한다.
    # 현재 보고 있던 웹페이지를 뒤로 가기 공간에 저장한다.
    # 앞으로 가기 공간에서 방문한지 가장 최근의 페이지에 접속한다, 그리고 해당 페이지는 앞으로 가기 공간에서 삭제된다.

    # 1개 이상의 페이지가 저장되어 있을 때만 2,3,번 과정이 실행된다.
    if len(frontStack) >= 1:
        # 현재 보고 있던 웹 페이지를 뒤로 가기 공간에 저장한다.
        backStack.append(now)
        # 앞으로 가기 공간에서 방문한지 가장 최근의 페이지에 접속한다.
        now = frontStack.pop()
        # 그리고 해당 페이지는 앞으로 가기 공간에서 삭제된다

    return now


def Access(backStack, frontStack, now, next):
    # 앞으로 가기 공간에 저장된 페이지가 모두 삭제된다.
    # 현재 페이지를 뒤로 가기 공간에 추가하고, 다음에 접속할 페이지가 현재 페이지르 갱신된다,
    # 단, 처음으로 웹페이지에 접속하는 경우라면 현재 페이지를 뒤로 가기 공간에 추가하지 않는다.

    # 앞으로 가기 공간에 저장된 페이지가 모두 삭제된다.
    frontStack.clear()
    # 처음으로 웹페이지에 접속하는 경우라면 현재 페이지를 뒤로 가기 공간에 추가하지 않는다.
    if now != None:
        # 현재 페이지를 뒤로가기 공간에 추가하고
        backStack.append(now)
    # 다음에 접속할 페이지가 현재 페이지로 갱신된다
    now = next

    return now


def Compress(backStack, now):

    tempStack = []
    before = None
    while backStack:
        temp = backStack.pop()
        if temp == before:
            continue
        else:
            tempStack.append(temp)
            before = temp

    if temp != before:
        tempStack.append(temp)

    while tempStack:
        backStack.append(tempStack.pop())


n, q = map(int, sys.stdin.readline().rstrip().split())

backStack = []
frontStack = []
now = None

for i in range(q):
    commend = sys.stdin.readline().rstrip().split(' ')

    if commend[0] == 'B':
        now = Back(backStack, frontStack, now)
    elif commend[0] == 'F':
        now = Front(backStack, frontStack, now)
    elif commend[0] == 'A':
        now = Access(backStack, frontStack, now, commend[1])
    elif commend[0] == 'C':
        Compress(backStack, now)


print(now)
if len(backStack) == 0:
    print(-1)
else:
    for i in reversed(backStack):
        print(i, end=' ')
    print()
if len(frontStack) == 0:
    print(-1)
else:
    for i in reversed(frontStack):
        print(i, end=' ')
