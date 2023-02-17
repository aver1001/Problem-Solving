import sys
from collections import deque
sys.stdin = open('input.txt', "r")

strs = sys.stdin.readline().rstrip()

# 팰린드롬이란 앞에서 읽었을 때와, 뒤에서부터 읽었을 때가 같은 문자열이다.

# 아래 4가지 연산으로 문자열을 팰린드롬으로 만든다.


def Insert():
    # 1. 문자열의 어떤 위치에 어떤 문자를 삽입 (시작과 끝도 가능)
    for iStr in insertList:
        for idx in range(N+1):
            temp = string[:idx]+iStr+string[idx:]
            if temp not in check:
                if isPalindrome(temp):
                    print(cnt + 1)
                    exit()
                queue.append((temp, cnt+1, state))
                check.add(temp)


def Delete():
    # 2. 어떤 위치에 있는 문자를 삭제
    for idx in range(N):
        temp = string[:idx]+' '+string[idx+1:]
        if temp not in check:
            if isPalindrome(temp):
                print(cnt + 1)
                exit()
            queue.append((temp, cnt+1, state))
            check.add(temp)


def Change():
    # 3. 어떤 위치에 있는 문자를 교체
    for iStr in insertList:
        for idx in range(N):
            temp = string[:idx]+iStr+string[idx+1:]
            if temp not in check:
                if isPalindrome(temp):
                    print(cnt + 1)
                    exit()
                queue.append((temp, cnt+1, state))
                check.add(temp)


def twoLocChange():
    # 4. 서로 다른 문자의 위치를 교환
    stringList = list(string)

    for i in range(N):
        for j in range(i+1, N):
            if stringList[i] != stringList[j]:
                stringList[i], stringList[j] = stringList[j], stringList[i]
                temp = ''.join(stringList)
                if temp not in check:
                    if isPalindrome(temp):
                        print(cnt + 1)
                        exit()
                    queue.append((temp, cnt+1, True))
                    check.add(temp)
                stringList[i], stringList[j] = stringList[j], stringList[i]


def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# 1,2,3 연산은 마음껏 사용 할 수 있지만, 4번 연산은 한번만 사용할 수 있다.
# 문자열이 주어졋을때, 팰린듣롬으로 만들기 위한 연산의 최솟값을 출력하라.

# 문자열의 길이는 최대 50 이다.


# 할수있는 경우의수 BFS 로 돌리면서 DP ?
if isPalindrome(strs):
    print(0)
    exit()
# [문자열,실행횟수,4번실행여부]
queue = deque([[strs, 0, False]])
N = len(strs)
insertList = set(list(strs))
check = set()
check.add(strs)
while queue:
    string, cnt, state = queue.popleft()

    # 1
    Insert()
    # 2
    Delete()
    # 3
    Change()
    # 4
    if state == False:
        twoLocChange()


'''
d   a   b   b   a


  

'''