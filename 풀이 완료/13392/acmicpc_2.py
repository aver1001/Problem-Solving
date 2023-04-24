import sys
sys.stdin = open('input.txt', "r")

# 재귀깊이해제
sys.setrecursionlimit(100000)

# go : 현재 idx번째 인덱스이고 위층에서 전체 left만큼 돌렸을 때 목표 숫자를 맞추기 위해 필요한 최소 조작 수를 리턴하는 함수
def go(idx, left):
    # Base Case : 모두 돌린경우
    if idx == n:
        return 0
    # Memoization
    if dp[idx][left] != -1:
        return dp[idx][left]
    dp[idx][left] = 9876543210
    # 위층에서 돌린 만큼 현재 숫자 재정의
    if left:
        now = (arr[idx] + left) % 10
    else:
        now = arr[idx]
    # 점화식
                        #원래 자신의 값, 다음칸에서의 
    dp[idx][left] = min(dp[idx][left], go(idx + 1, (left + left_cache[now][res[idx]]) % 10) + left_cache[now][res[idx]])
    dp[idx][left] = min(dp[idx][left], go(idx + 1, left) + right_cache[now][res[idx]])
    return dp[idx][left]

# left_cache : 현재 수가 i, 맞춰야 하는 수가 j일 때 왼쪽으로 몇칸 돌려야 하는지를 저장하는 2차원 배열
left_cache = [[-1] * 10 for _ in range(10)]

# right_cache : 현재 수가 i, 맞춰야 하는 수가 j일 때 오른쪽으로 몇칸 돌려야 하는지를 저장하는 2차원 배열
right_cache = [[-1] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        temp = 0
        while True:
            if (i + temp) % 10 == j:
                break
            temp += 1
        left_cache[i][j] = temp
        temp = 0
        while True:
            if (i - temp) % 10 == j:
                break
            temp += 1
        right_cache[i][j] = temp

# 입력부 및 정답출력
n = int(sys.stdin.readline())
dp = [[-1] * 10 for _ in range(n)]
arr = list(map(int, sys.stdin.readline().rstrip()))
res = list(map(int, sys.stdin.readline().rstrip()))
print(go(0, 0))