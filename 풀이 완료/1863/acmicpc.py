import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
stack = []
board = []
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    board.append([x, y])

for x, y in board:

    while True:
        if len(stack) == 0:
            stack.append(y)
            break
        # 다음 들어올게 작다면
        if stack[-1] > y:
            stack.pop()
            answer += 1
        elif stack[-1] == y:
            stack.pop()
        else:
            stack.append(y)
            break


for i in stack:
    if i != 0:
        answer += 1
print(answer)
