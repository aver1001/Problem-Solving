import sys
sys.stdin = open('input.txt', "r")

X, K = map(int, sys.stdin.readline().rstrip().split(' '))

'''
문제
두 자연수 X와 K가 주어진다. 그러면, 다음 식을 만족하는 K번째로 작은 자연수 Y를 찾아야 한다.

X + Y = X | Y

|는 비트 연산 OR이다.

입력
첫째 줄에 X와 K가 주어진다. X와 K는 2,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 X + Y = X | Y를 만족하는 K번째 작은 Y를 출력한다. 정답은 231-1 보다 클 수도 있다.
'''
X = bin(X)[2:]
X = X[::-1]
K = bin(K)[2:]
K = K[::-1]
pt = 0
answer = ''
for x in X:

    if x == '0':
        answer = K[pt]+answer
        pt += 1
    else:
        answer = '0' + answer

    if pt == len(K):
        break

while len(K) != pt:
    answer = K[pt] + answer
    pt += 1

print(int('0b'+answer, 2))
