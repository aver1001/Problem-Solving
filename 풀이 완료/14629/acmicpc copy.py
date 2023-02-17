import sys
from itertools import permutations
sys.stdin = open('input.txt', "r")

'''

'''
N = int(sys.stdin.readline().rstrip())

# 나올수 있는 경우
# 자리수 넘어서 더 클경우
# 같은자릿수에서 더 클경우
# 같은 자릿수에서 더 작을경우
# 낮은 자리에서 더 작을경우

Nlen = len(str(N))

# 자리수 넘어서 더 클경우


def makeNumber(num,check,floor,state):
    
    if state == 'overUpper':
        if floor == N+1:
            
    
    for i in range (10):
        if check[i] == False:
            check[i] = True
            makeNumber(num+str(i),check,floor+1)
            check[i] = False