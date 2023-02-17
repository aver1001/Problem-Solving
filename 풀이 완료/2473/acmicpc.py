import sys
sys.stdin = open('input.txt', "r")


N = int(sys.stdin.readline().rstrip())
water = list(map(int, sys.stdin.readline().rstrip().split(' ')))
water.sort()
Min = 3000000000
lt, rt, mt = 0, 2, 1

while lt < rt and rt < N:
    # lt,rt 움직이기

    while mt < rt:
        # mt 움직이기
        if abs(water[lt]+water[mt]+water[rt]) < Min:
            Min = abs(water[lt]+water[mt]+water[rt])
            answer = [water[lt], water[mt], water[rt]]

        # mt는 점점 큰걸 더할것임

        # lt+mt+rt가 양수라면 더 확인할 필요 없고.
        if water[lt]+water[mt]+water[rt] > 0:
            break
        # lt+mt+rt가 음수라면 더 확인해봐야함.
        elif water[lt]+water[mt]+water[rt] < 0:
            mt += 1
        # lt+mt+rt가 0이라면 이거 하면됨
        else:
            print(answer)
            exit()

    # 여기서 구한 최솟값이 양수라면 lt를 줄여야하고
    if sum(answer) > 0:
        break
    # 여기서 구한 최솟값이 음수라면 rt를 늘려야함.
    else:
        rt += 1
        mt = lt+1

print(answer)
