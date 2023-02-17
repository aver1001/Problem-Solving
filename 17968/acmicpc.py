import sys
sys.stdin = open('input.txt', "r")
'''
[백준 17968 Fire on Field] S4
DP인듯
1:22 ~ 1:32 (10분 소요)


A를 아래와 같은 규칙을 따르는 양의 정수들로 이루어진 수열이라고 하자.
> 
(1) A[0] = 1, A[1] = 1 으로 고정.

(2) i가 2이상일 때, A[i]는 아래 조건을 만족하는 가장 작은 정수이다.

K>0 이고  i-2k >= 0일 때 
A[i] - A[i-k] != A[i-k] - A[I-2k] 를 만족하는 가장 작은 수

Ex) i = 2,
A[2] - A[2-k] != A[2-k] - A[i-2k]
K = 1일때 
A[2] - A[1] != A[1] - A[0]
A[2] -1 != 1 - 1
A[2]가 1이면 위 식을 만족하지 못하고 A[2]가 2라면 위 식을 만족하므로 A[2] = 2가 된다.


따라서 수열은 하나로만 정의될 수 밖에 없다.
A[0] = 1, A[1] = 1, A[2] = 2, A[3] = 1, A[4] = 1, A[5] = 2, A[6] = 2, A[7] = 4, A[8] = 4 … 

이 때 정수 n이 인풋으로 주어질 때 A[n]의 값을 구하여라

0 < K <= i/2
A[i] != 2A[i-k]-A[i-2k]

i == 3
0 < K <= 3/2
K = 1
A[3] != 2A[2]-A[1]
A[3] != 4-1
A[3] != 3
A[3] == 1

i == 4
0< K <= 2
K = 1
A[4] != 2A[3]-A[2]
A[4] != 2-2
A[4] != 0

K = 2
A[4] != 2A[2]-A[0]
A[4] != 4-1
A[4] != 3

A == 1

'''


def find(i):
    table = set()
    for k in range(1, i//2 + 1):
        table.add(2*A[i-k]-A[i-2*k])
    for idx in range(1, 1001):
        if idx not in table:
            return idx


A = [0]*1001
A[0] = 1
A[1] = 1
N = int(sys.stdin.readline().rstrip())
for i in range(2, N+1):
    A[i] = find(i)

print(A[N])
