import sys
sys.stdin = open('input.txt', "r")

strs = input()

answer = ''
for s in strs:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)