import sys
from itertools import product

sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
commend = list(sys.stdin.readline().rstrip().split(' '))

'''
채널 N으로 이동
고장난 버튼의 개수 M
고장난 버튼
'''

# 수빈이가 지금 보고잇는 채널은 100번
start = 100
number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
answer = abs(N - 100)
if commend != ['']:
    for c in commend:
        number.remove(c)

for i in range(len(str(N))-1, len(str(N))+2):
    if i >= 1:
        for num in product(number, repeat=i):
            answer = min(answer, abs(N - int(''.join(list(num))))+i)
print(answer)
