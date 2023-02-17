import sys
sys.stdin = open('input.txt', "r")

'''
계단수
    인접한 모든 자리의 차이가 1
주어진 문제
    N이 주어졌을때 길이가 N이며 0에서 9까지의 숫자가 모두 등장하는
    계단수의 개수
'''

N = int(sys.stdin.readline().rstrip())

# 최대 N == 100

DP = [[[-1]*10 for _ in range(1 << 10)] for _ in range(100)]


def DFS(num, left, check, temp):
    #print(num, left, check)

    if left == 0:
        if check == (1 << 10) - 1:

            DP[left][check][num] = 1
        else:
            DP[left][check][num] = 0
        return DP[left][check][num]

    if DP[left][check][num] == -1:
        answer = 0
        if num + 1 <= 9:
            answer += DFS(num + 1, left-1, check | 1 <<
                          (num+1), temp+str(num+1))
        if num - 1 >= 0:
            answer += DFS(num - 1, left-1, check | 1 <<
                          (num-1), temp+str(num-1))

        DP[left][check][num] = answer % 1_000_000_000
        return answer
    else:
        return DP[left][check][num]


answer = 0
for i in range(1, 10):
    answer += (DFS(i, N-1, 1 << i, str(i)))
print(answer % 1_000_000_000)
