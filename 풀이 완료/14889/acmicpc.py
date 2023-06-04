import sys
from itertools import combinations
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
score = []
for _ in range (N):
    score.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

allMember = set(range(N))
answer = sys.maxsize

for teamA in combinations(range(N),N//2):

    teamB = allMember-set(teamA)
    scoreA = scoreB = 0
    
    for i,j in list(combinations(teamA, 2)):
        scoreA += score[i][j]
        scoreA += score[j][i]
    for i,j in list(combinations(teamB, 2)):
        scoreB += score[i][j]
        scoreB += score[j][i]
                
    answer = min(answer,abs(scoreA-scoreB))
    
print(answer)