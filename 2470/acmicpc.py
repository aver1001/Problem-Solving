import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
commend = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# 산성이나 알칼리로만 주어지는 경우도 있다 => 산성 알칼리 나눠서 계산하면 안됨.
# 일단 정렬 후 푸는게 맞는 것 같음.

commend.sort()

# lt rt 두고

# lt==rt break
# 현재 최솟값보다 작다면
# 결과 배열 업데이트 후
#rt -= 1
# 크다면
#lt += 1
# 같다면
# 결과 배열에 추가

answer = 1_000_000_000 * 2
water = []

lt = 0
rt = len(commend)-1

while lt < rt:
    hap = commend[lt] + commend[rt]

    if abs(hap) < answer:
        answer = abs(hap)
        water = [commend[lt], commend[rt]]

    if hap < 0:
        lt += 1

    else:
        rt -= 1
print(*water)
