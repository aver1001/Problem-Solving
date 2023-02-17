import sys
sys.stdin = open('input.txt', "r")
'''
1. 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 합니다.
2. 같은 그림을 두 번 이상 사는 것은 불가능합니다.
'''
N = int(sys.stdin.readline().rstrip())


def solution(n, arr):
    M = [[[0] * 10 for j in range(1 << n)]
         for i in range(n)]  # M[artist][path(bin)][price]

    def dfs(artist, path, price):
        if M[artist][path][price] != 0:  # 메모제이션 적용
            return M[artist][path][price]

        count = 0  # 현재 artist 부터의 최대 거래 횟수
        for nextA in range(1, n):
            if arr[artist][nextA] < price or path & (1 << nextA) > 0:
                continue
            count = max(count, 1 + dfs(nextA, path |
                        (1 << nextA), arr[artist][nextA]))
        M[artist][path][price] = count  # 메모!

        return count

    return 1 + dfs(0, 1, 0)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append([int(j) for j in input().strip()])
    result = solution(n, arr)
    print(result)
