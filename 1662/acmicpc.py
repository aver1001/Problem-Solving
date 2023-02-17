import sys
sys.stdin = open('input.txt', "r")

S = sys.stdin.readline().rstrip()

pt = 0
N = len(S)
stack = []

while True:

    if S[pt] == '(':
        stack.append(S[pt])
    elif S[pt] == ')':
        cnt = 0
        while True:
            temp = stack.pop()
            if type(temp) == int:
                cnt += temp
                continue
            if temp == '(':
                break
            cnt += 1

        stack.append(cnt * int(stack.pop()))
    else:
        stack.append(S[pt])
    pt += 1

    if pt == N:
        break

answer = 0
for i in stack:
    if type(i) == str:
        answer += 1
    else:
        answer += i

print(answer)
