import sys
sys.stdin = open('input.txt', "r")
D = int(sys.stdin.readline().rstrip())

MOD = 1_000_000_007
SIZE = 8

def multiply_matrix(matrix1, matrix2):
    return [[sum(matrix1[i][k]*matrix2[k][j] % MOD for k in range(SIZE)) % MOD
             for j in range(SIZE)] for i in range(SIZE)]
    


# dp 초기화
dp1 = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]]

dp2 = [[0]*SIZE for _ in range(SIZE)]
for i in range(SIZE):
    dp2[i][i] = 1
    
    # 분할 정복
while D > 0:
    #2로 나누어 떨어지지 않는다면.
    if D % 2 != 0:
        #행렬을 한번 곱해준다.
        dp2 = multiply_matrix(dp2, dp1)
        D -= 1
    #2로 나누어 떨어진다면
    else:
        #dp1을 제곱한다.
        dp1 = multiply_matrix(dp1, dp1)
        D //= 2

print(dp2[0][0])