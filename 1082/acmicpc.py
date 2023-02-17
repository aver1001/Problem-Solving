import sys
sys.stdin = open('input.txt', "r")
'''
가격 : 숫자 딕셔너리로 DP 진행한다.
새 딕셔너리를 만든 뒤
이전 딕셔너리를 다 돌면서 새 딕셔너리에 모든숫자를 더한 값(벨류), 가격(키값)을 추가해준다.
이떄 전에 만들어 놓은 딕셔너리는 신경을 쓸 필요가 없다 => 아무리 큰숫자도 자리수가 늘어나는게 유리하기 때문
만약 새 딕셔너리에 이미 데이터가 있다면 숫자를 비교해서 더큰 숫자로 바꿔준다.
반복 진행하다보면 언젠가 진행이 안되는 지점이 올 것임.
그때 break 하고 벨류중 최대값을 리턴해주면 됨
'''


N = int(sys.stdin.readline().rstrip())
costs = list(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())

# 1~ N-1 까지 만들수 있는 경우와 금액 초기화
# 같은 가격이면 높은숫자가 유리하기 떄문에 같다면 교체해도 상관없음.
table = {costs[i]: i for i in range(N) if costs[i] <= M}
while True:
    # 작업을 진행했는지를 확인
    isProcess = False
    tempTable = {}

    for cost, num in table.items():

        # 숫자가 0일경우 처리
        if num == 0:
            continue

        for idx in range(N):
            nextNum = num*10 + idx
            nextCost = cost + costs[idx]

            # 가격 넘어가면 실행하지 않음.
            if nextCost > M:
                continue

            # 아직 도달하지 못한 가격이거나 지금 만든 숫자가 더 클경우
            if nextCost not in tempTable or tempTable[nextCost] < nextNum:
                # 업데이트 해준다
                isProcess = True
                tempTable[nextCost] = nextNum

    if isProcess == False:
        break
    # table 변경
    table = tempTable


print(max(table.values()))
