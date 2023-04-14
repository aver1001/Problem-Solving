import sys
import time
sys.stdin = open('input.txt', "r")

strs = list(input())
bomb = list(input())


while True:
    tempStrs = ''
    isBomb = False
    stack = []
    for s in strs:
        
        stack.append(s)
        if len(stack) >= len(bomb):
            
            if stack[-len(bomb):] == bomb:
                #print(stack[-len(bomb):],bomb)
                for _ in range (len(bomb)):
                    stack.pop()
                isBomb = True
    if isBomb == False:
        break
    strs = stack
if len(strs) == 0:
    print("FRULA")
else:
    print(''.join(strs))