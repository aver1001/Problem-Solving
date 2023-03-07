import sys
from itertools import permutations
from collections import deque
sys.stdin = open('input.txt', "r")

'''
안타: 1
2루타: 2
3루타: 3
홈런: 4
아웃: 0
'''

def playGame(player):
    
    idx = 0
    E = 0
    score = 0
    base = deque([0,0,0])
    out = 0
    
    while True:
        if idx < 3:
            target = player[idx]
        elif idx == 3:
            target = 0
        else:
            target = player[idx-1]

        if Score[E][target] == 0:
            out += 1
            
        elif Score[E][target] == 1:
            if base.popleft() == 1:
                score += 1
            base.append(1)
            
        elif Score[E][target] == 2:
            if base.popleft() == 1:
                score += 1
            base.append(1)
            
            if base.popleft() == 1:
                score += 1
            base.append(0)
            
            
        elif Score[E][target] == 3:
            if base.popleft() == 1:
                score += 1
            base.append(1)
            
            if base.popleft() == 1:
                score += 1
            base.append(0)
            
            if base.popleft() == 1:
                score += 1
            base.append(0)
            
        elif Score[E][target] == 4:
            if base.popleft() == 1:
                score += 1
            
            if base.popleft() == 1:
                score += 1
            
            if base.popleft() == 1:
                score += 1
                
            score += 1
            
            base = deque([0,0,0])
            
        idx += 1
        idx %= 9
        
        if out == 3:
            out = 0
            E += 1

            base = deque([0,0,0])
            if E == N:
                return score
            
                
            


N = int(sys.stdin.readline().rstrip())
    
Score = []
answer = 0
for _ in range (N):
    Score.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for p in permutations([1,2,3,4,5,6,7,8],8):
    answer = max(playGame(p),answer)
print(answer)
            
            

            
    
