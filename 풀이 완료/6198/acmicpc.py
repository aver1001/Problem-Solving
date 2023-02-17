import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
stack = []
answer = 0
building = []
for _ in range(N):
    building.append(int(sys.stdin.readline().rstrip()))
for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()

    stack.append(building[i])
    answer += len(stack) - 1

print(answer)
