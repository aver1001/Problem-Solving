import sys
sys.stdin = open('input.txt', "r")
'''
N명의 학생들을 키 순서대로 줄 세운다.
키를 잴 수 있는 마땅한 방법이 없어서 두 학생의 키를 비교해서 줄을 세울것.
M번의 키 비교 결과가 주어짐.
입력 A,B는 A가 B보다 크다는 의미.
'''

N, M = map(int, sys.stdin.readline().rstrip().split())
table = {i:{'in':set(),'out':set()} for i in range (1,N+1)}

for _ in range (M):
    
    A,B = map(int, sys.stdin.readline().rstrip().split())
    # A가 등장하기 위헤선 B가 먼져 등장해야함.
    table[A]['in'].add(B)
    table[B]['out'].add(A)

stack = []
for key,values in table.items():
    if len(values['in']) == 0:
        stack.append(key)

# 이제 진입차수가 0인것들부터 시작해서 지우주면서 찾아줌.

answer = []
while stack:
    Loc = stack.pop()
    answer.append(Loc)
    for nextLoc in table[Loc]['out']:
        table[nextLoc]['in'].remove(Loc)
        if len(table[nextLoc]['in']) == 0:
            stack.append(nextLoc)
                
print(*reversed(answer))