import sys
sys.stdin = open('input.txt', "r")

strs = sys.stdin.readline().rstrip()

# 팰린드롬이란 앞에서 읽었을 때와, 뒤에서부터 읽었을 때가 같은 문자열이다.

# 아래 4가지 연산으로 문자열을 팰린드롬으로 만든다.x

# 1,2,3 연산은 마음껏 사용 할 수 있지만, 4번 연산은 한번만 사용할 수 있다.
# 문자열이 주어졋을때, 팰린듣롬으로 만들기 위한 연산의 최솟값을 출력하라.

# 문자열의 길이는 최대 50 이다.


# 할수있는 경우의수 BFS 로 돌리면서 DP ?

# [문자열,실행횟수,4번실행여부]
N = len(strs)


def DFS(left, right):

    if DP[left][right] != -1:
        return DP[left][right]

    if left >= right:
        return 0

    if strs[left] == strs[right]:
        DP[left][right] = min(DFS(left+1, right)+1,
                              DFS(left, right-1)+1, DFS(left+1, right-1))

    else:
        DP[left][right] = min(DFS(left+1, right)+1,
                              DFS(left, right-1)+1, DFS(left+1, right-1)+1)

    return DP[left][right]


DP = [[-1] * N for _ in range(N)]
answer = DFS(0, N-1)

stringList = list(strs)
for i in range(N):
    for j in range(i+1, N):
        DP = [[-1] * N for _ in range(N)]
        if stringList[i] != stringList[j]:
            stringList[i], stringList[j] = stringList[j], stringList[i]
            strs = ''.join(stringList)
            answer = min(DFS(0, N-1)+1, answer)
            stringList[i], stringList[j] = stringList[j], stringList[i]

print(answer)
