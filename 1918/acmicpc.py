import sys
sys.stdin = open('input.txt', "r")

str = sys.stdin.readline().rstrip()

answer = ''
stack = []
flag = False
for s in str:
    if s.isalpha():
        answer += s
        if flag:
            flag = False
            while stack:
                temp = stack.pop()
                if temp == '(':
                    stack.append('(')
                    break
                answer += temp

    else:
        if s == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                answer += temp

        elif s == '/' or s == '*':
            flag = True
            stack.append(s)
        else:
            stack.append(s)

while stack:
    temp = stack.pop()
    answer += temp

print(answer)
# 문자열은 만나는대로 더해줌
# ) 나오면 ( 나올때까지 연산자 더해줌
