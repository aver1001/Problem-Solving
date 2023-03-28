import sys
sys.stdin = open('input.txt', "r")

def bimatch(x):
    
    if isVisited[x]:
        return False
    isVisited[x] = True
    
    for num in userDo[x]:
        if userChoise[num] == -1 or bimatch(userChoise[num]):
            userChoise[x] = num
            return True
        
    return False

N, M = map(int, sys.stdin.readline().rstrip().split())

userDo = []

for _ in range (N):
    userDo.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])

userChoise = [-1]*(M+1)
for i in range (N):
    isVisited = [False]*(N+1)
    bimatch(i)

for i in range (N):
    isVisited = [False]*(N+1)
    bimatch(i)

answer = 0
for num in userChoise:
    if num != -1:
        answer += 1
print(answer)