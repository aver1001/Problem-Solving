import sys
sys.stdin = open('input.txt', "r")


def combinations(aNum, bNum):

    temp = 1
    for i in range(aNum+bNum, 0, -1):
        temp *= i

    for i in range(aNum, 0, -1):
        temp = temp//i

    for i in range(bNum, 0, -1):
        temp = temp//i

    return temp


N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))


# 일단 범위안에 들어오는지부터 확인하자.
Maximum = combinations(N, M)
if Maximum < K:
    print(-1)
    exit()

lt, rt = 0, Maximum
answer = ''
while (N != 0 and M != 0):
    '''
    a를 넣엇을때 가능한 범위와
    b를 넣엇을때 가능한 범위를 구한다.
    구한뒤, 가능성이 있는곳으로 움직여준다.
    '''

    # a를 넣엇을 경우
    inputA = combinations(N-1, M)
    # z를 넣엇을 경우
    inputZ = combinations(N, M-1)

    # a 를 넣었을 경우 범위를 만족한다면.
    if lt <= K <= lt+inputA:
        rt = lt+inputA
        answer += 'a'
        N -= 1
    # z 를 넣엇을경우 범위를 만족한다면.
    else:
        lt = lt+inputA
        answer += 'z'
        M -= 1

while N != 0:
    answer += 'a'
    N -= 1

while M != 0:
    answer += 'z'
    M -= 1
print(answer)
