import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())


for _ in range(N):
    table = {}
    isBefore = set()
    F = int(sys.stdin.readline().rstrip())
    for _ in range(F):
        A, B = sys.stdin.readline().rstrip().split(' ')

        # 둘다 처음
        if A not in isBefore and B not in isBefore:
            # 아무거나 하나 부모노드로 설정해준다
            table[A] = {B}
        # B는 존재 A는 처음
        elif A not in isBefore and B in isBefore:
            # 부모로 존재할경우
            if B in table:
                table[B].add(A)
            else:
                # 자식으로 존재할경우
                for key, value in table.items():
                    if B in value:
                        table[key].add(A)

        # A는 존재 B는 처음
        elif A in isBefore and B not in isBefore:
            # 부모로 존재할경우
            if A in table:
                table[A].add(B)
            else:
                # 자식으로 존재할경우
                for key, value in table.items():
                    if A in value:
                        table[key].add(B)
        # 둘다 존재할경우
        else:

            # 둘다 부모일경우
            if A in table and B in table:
                table[A].update(table[B])
                table[A].add(B)
                del table[B]
            # A만 부모일경우
            elif A in table and B not in table:
                for key, value in table.items():
                    if B in value:
                        if key == A:
                            break
                        table[A].update(table[key])
                        table[A].add(key)
                        del table[key]
                        break

            # B만 부모인경우
            elif A not in table and B in table:
                for key, value in table.items():
                    if A in value:
                        if key == B:
                            break
                        table[B].update(table[key])
                        table[B].add(key)
                        del table[key]
                        break
            # 둘다 자식인경우
            else:

                for key, value in table.items():
                    if A in value:
                        Amother = key
                        break

                for key, value in table.items():
                    if B in value:
                        Bmother = key
                        break

                if Amother != Bmother:
                    table[Amother].update(table[Bmother])
                    table[Amother].add(Bmother)
                    del table[Bmother]

        isBefore.add(A)
        isBefore.add(B)

        if A in table:
            print(len(table[A])+1)
        elif B in table:
            print(len(table[B])+1)
        else:
            for key, value in table.items():
                if A in value:
                    print(len(table[key])+1)
