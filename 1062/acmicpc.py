import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

N, K = map(int, sys.stdin.readline().rstrip().split())

answer = 0
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
# antic 이 다섯개는 들어가야 뭘 읽던 말던함
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

require = {'a', 'n', 't', 'i', 'c'}
Array = []
for word in words:
    check = set()

    for i in word:
        if i not in require:
            check.add(i)

    # 우리가 가르칠수 있는 여유문자는 K-5 개
    # 그거보다 큰거는 확인할 필요 없음

    if len(check) > K-5:
        continue

    Array.append(check)
alpha = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
         'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0
for study in combinations(alpha, K-5):
    cnt = 0
    for A in Array:
        for char in A:
            if char not in study:
                break
        else:
            cnt += 1

    if cnt > answer:
        answer = cnt
print(answer)
