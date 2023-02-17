import sys
import math
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())

target = []
answer = []
for i in range(1, int(N**(1/2))+1):
    # 만약 나머지가 0이라면 약수임
    if N % i == 0 and N//i != i:
        target.append([i, N//i])


for sub, hap in target:

    # a+b가 짝수일경우
    if hap % 2 == 0:
        num1 = hap // 2
        num2 = hap // 2

        num2 += sub//2
        num1 += -(sub//2)

    # a+b가 홀수일경우
    else:
        num1 = hap // 2
        num2 = hap // 2 + 1

        num2 += (sub-1) // 2
        num1 += -((sub-1) // 2)

    if num2**2 - num1**2 == N:
        answer.append(num2)


answer.sort()
if answer == []:
    print(-1)
    exit()
for i in answer:
    print(i)
