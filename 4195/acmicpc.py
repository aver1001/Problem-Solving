import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
F = int(sys.stdin.readline().rstrip())
table = {}
for _ in range(F):
    A, B = sys.stdin.readline().rstrip().split(' ')
    # 처음

    # 부모노드에 있는지 확인
    if A in table and B in table:
        table[A]['cnt'] += table[B]['cnt']
        continue
    elif A in table:
        table[A][B] = {}
        table[A]['cnt'] += 1
    elif B in table:
        table[B][A] = {}
        table[B]['cnt'] += 1

        # 자식노드에 존재하는지 확인
    else:

        for key, values in table.items():

            # 자식노드에 존재한다면
            if A in values and B in values:
                # 둘다 존재할경우 continue
                continue
            elif A in values:
                # A만 존재할경우 B를 부모노드의 자식으로 추가
                table[key][B] = {}
                table[key]['cnt'] += 1
                break
            elif B in values:
                table[key][A] = {}
                table[key]['cnt'] += 1
                break
        else:
            table[A] = {'cnt': 2}
            table[A][B] = {}

