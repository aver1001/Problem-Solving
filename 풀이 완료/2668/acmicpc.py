import sys
sys.stdin = open('input.txt', "r")

def dfs(x:int,tempChoose:set):
    
    #사이클 발생
    if x in tempChoose:
        

N = int(sys.stdin.readline().rstrip())

numbers = [0]
for _ in range (N):
    numbers.append(int(sys.stdin.readline().rstrip()))
    



Choose = set()
answer = 0

for idx in range(1,N+1):
    if idx not in Choose:
        dfs(idx,set())
