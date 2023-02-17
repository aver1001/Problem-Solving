import sys
sys.stdin = open('input.txt', "r")

str = sys.stdin.readline().rstrip()

answer = ''
stack = []
for s in str:
    # 숫자
    if s.isalpha():
        answer += s
    # 연산자
    else:
        # 우선순위 높은 연산자
        if s in {'*', '/'}:
            while stack and stack[-1] in {'*', '/'}:
                answer += stack.pop()
            stack.append(s)
        # 우선순위 낮은 연산자
        elif s in {'+', '-'}:
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(s)
        # 여는 괄호
        elif s == '(':
            stack.append(s)
        # 닫는 괄호
        elif s == ')':
            while stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()
print(answer)
