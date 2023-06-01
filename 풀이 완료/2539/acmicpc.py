import sys
sys.stdin = open('input.txt', "r")

Y, X = map(int, sys.stdin.readline().rstrip().split())
papaerN = int(sys.stdin.readline().rstrip())
blankN = int(sys.stdin.readline().rstrip())
yMax = 0
xMax = 0
blank = []
for _ in range(blankN):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    yMax = max(yMax, y)
    xMax = max(xMax, x)
    blank.append([y, x])


def usePapaer(length):
    start = blank[0][1]
    count = 1
    for _, x in blank:
        if x >= start + length:
            start = x
            count += 1

    return count


'''
1. 사용되는 색종이는 모두 크기가 같고 정사각형 모양이다.
2. 색종이 크기는 한 변의 길이로 나타내며, 원하는 크기의 색종이는 모두 구할 수 있다.
3. 모든 색종이는 반드시 도화지의 밑변에 맞추어 붙인다. 이때 색종이를 겹쳐서 붙일 수 있다.

모든 색종이는 반드시 도화지의 밑변에 맞추어 붙인다 -> y좌표중 가장 큰것보다는 색종이의 크기가 커야함.

x좌표로 힌트를 얻을수 있는건 없을까?
(잘못 칠한 칸의 시작 - 끝의 길이 / 색종이의 최대갯수) 보다 한변의 크기가 크거나 같아야함.

그럼 결국 한변의 길이는
max ((잘못 칠한 칸의 시작 - 끝의 길이 / 색종이의 최대갯수), 잘못칠한 y의 최대) <= 한변의 길이

'''

blank.sort(key=lambda x: x[1])

lt = yMax
rt = 1000001
answer = 0

while lt <= rt:
    mid = (lt+rt) // 2

    # 종이가 부족함 == 길이를 늘려야함
    if usePapaer(mid) <= papaerN:
        answer = mid
        rt = mid - 1
    else:
        rt = mid + 1

print(answer)
