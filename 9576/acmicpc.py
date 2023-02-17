import sys
sys.stdin = open('input.txt', "r")
'''
백준이는 N권의 책을 나눠준다.
책은 1~N 까지의 번호가 있다.

학부생이 M명 있다.
학부생들은 a,b 를 제출하게되고, a이상 b 이하인 책 중에서 남아있는 책 한권을 골라 학생에게 준다.

가장 많은학생에게 책을 주는 방법은?


'''
for _ in range(int(sys.stdin.readline().rstrip())):
    N, M = map(int, sys.stdin.readline().rstrip().split(' '))

    isBorrow = [False] * (N+1)
    answer = 0
    board = []
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
        board.append([a, b])
    board.sort(key=lambda x: (x[1], x[0]))
    for a, b in board:
        print(a, b)
        for idx in range(a, b+1):
            if isBorrow[idx] == False:
                answer += 1
                isBorrow[idx] = True
                break
        print(isBorrow)

    print(answer)
