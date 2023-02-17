import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
chews = list(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())
gems = map(int, sys.stdin.readline().rstrip().split(' '))

# 추를 이용해서 gem의 무개를 잴 수 있나?
# 추의 개수 30개 이하.
# 구슬의 개수는 7개 이하

# 추를 이용해서 만들 수 있는 무개를 구함?


# 추의개수 크기 만큼의 set을 가진 배열을 선언해 준다
table = [set() for _ in range(N)]
doit = set()

# 추의 무개를 순회하며
for weight in chews:
    temp = [set() for _ in range(N)]

    for idx in range(N-1):

        for setWeight in table[idx]:
            if setWeight + weight not in table[idx+1]:
                temp[idx+1].add(setWeight+weight)
                doit.add(setWeight+weight)

            if abs(setWeight - weight) not in table[idx+1]:
                temp[idx+1].add(abs(setWeight - weight))
                doit.add(abs(setWeight - weight))

    for idx in range(N):
        if idx == 0:
            table[idx].add(weight)
            doit.add(weight)
        else:
            table[idx].update(temp[idx])

for g in gems:
    if g in doit:
        print('Y', end=' ')
    else:
        print('N', end=' ')
