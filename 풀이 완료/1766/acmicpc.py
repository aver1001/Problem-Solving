from gettext import find
import sys
sys.stdin = open('input.txt', "r")
'''
문제는 난이도 순서로 출제되어 있다.
1이 쉬운거 N이 어려운거

문제간의 관계가 있는 경우가 있다.

1. N개의 문제는 모두 풀어야 한다.
2. 먼저 푸는 것이 좋은 문제가 잇는 문제는, 반드시 먼져 풀어야한다.
3. 가능하다면 쉬운문제부터 풀어야 한다.

'''
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
table = {i: [] for i in range(1, N+1)}
for _ in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split(' '))
    # 문제 : 선수문제
    table[second].append(first)

for idx in range(1, N+1):
    table[idx].sort(reverse=True)

print(table)
answer = []
isSolved = set()


def findMatter(idx):

    # 선수과목이 없다면 풀어준다.
    if table[idx] == [] and idx not in isSolved:
        answer.append(idx)
        isSolved.add(idx)
    # 문제를 풀어줬다면
    # elif table[idx] == []:
    #     return
    # 만약 선수과목이 있다면 재귀적으로 선수과목을 찾아준다.
    else:
        while table[idx]:
            nextPro = table[idx].pop()
            if nextPro not in isSolved:
                isSolved.add(nextPro)
                findMatter(nextPro)
                answer.append(nextPro)

    if idx not in isSolved:
        answer.append(idx)
        isSolved.add(idx)


for i in range(1, N+1):
    # 1번부터 순회하면서 선수과목이 없다면 풀어준다.
    findMatter(i)

print(answer)
