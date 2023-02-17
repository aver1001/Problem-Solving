import sys
import heapq
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
postiveNums = []
negativeNums = []
answer = 0

for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp > 0:
        postiveNums.append(temp)
    else:
        negativeNums.append(temp)

postiveNums.sort(reverse=True)
negativeNums.sort()

for nums in [postiveNums, negativeNums]:
    for idx in range(0, len(nums), 2):

        if idx + 1 >= len(nums):
            answer += nums[idx]
            break

        num1 = nums[idx]
        num2 = nums[idx+1]

        if num1 * num2 > num1+num2:
            answer += num1*num2
        else:
            answer += num1+num2


print(answer)
