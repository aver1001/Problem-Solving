import sys
sys.stdin = open('input.txt', "r")

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
table = {i: set() for i in range(1, N+1)}
for _ in range(M):
    commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    commend = commend[1:]
    for idx in range(len(commend)-1):
        table[commend[idx]].add(commend[idx+1])


answer = []
while table:
    isProcess = False
    delList = []
    for key, value in table.items():
        if len(value) == 0:
            answer.append(key)
            delList.append(key)
            isProcess = True

    for d in delList:
        del table[d]

    for key, value in table.items():

        for d in delList:
            if d in value:
                value.remove(d)

    if isProcess == False:
        print(0)
        exit()

answer.reverse()
for a in answer:
    print(a)
