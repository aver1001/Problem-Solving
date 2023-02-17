import sys
sys.stdin = open('input.txt', "r")

'''
[백준 23568 Find the House] S4

영희는 영희의 친구 지선이의 집을 찾기위해 1차원 도로에 서있다. 
지선이 집의 정확한 위치를 알기 위해서는, 영희는 지선에게 현재 위치를 담은 메시지를 보내야한다.(현재의 위치는 정수로 표현한다고 가정하자).
2분뒤에, 영희는 지선에게 3개의 정보로 이루어진 답장을 n개 받는다.

3개의 정보는 아래와 같다
- (i, j, k)에서 i는 현재의 위치를, j는 i에서 움직여야할 방향을(L: Left 또는 R: Right), k는 i에서 움직여야할 거리를 뜻한다. 
- (i, j, k), (i`, j`, k`) 에서 i != i` 이다.
- 모든 메시지들을 따라 위치를 옮기면 지선이의 집에 도착하게 된다.

예를들어, 영희의 현재 위치를 0이고
메시지가 
(3, R, 4)
(0, L, 2)
(7, L, 5)
(-2, R, 5) 가 들어왔다고 해보자.

영희는 처음 위치가 0이므로 (0, L, 2)에 따라 -2로 이동하게된다.
그 후엔 영희의 위치는 -2 이므로 (-2, R, 5)를 따르게 되고 
차례로 (3, R, 4) -> (7, L, 5)를 따르게 된다. 결국엔 목적지로 2에 도착하게 되고 그 곳이 지선이의 집이다.

입력이 들어왔을 때 지선이의 집의 위치를 구하여라

'''
# 답장 저장할 table 선언
table = {}
N = int(sys.stdin.readline().rstrip())
for _ in range(N):

    Loc, direct, distance = sys.stdin.readline().rstrip().split(' ')

    Loc = int(Loc)
    distance = int(distance)

    # table에 key값으로 자신의 위치 넣어주고
    # value값으로 [방향,거리] 넣어줌
    table[Loc] = [direct, distance]

Now = int(sys.stdin.readline().rstrip())

while True:

    # 더이상 갈곳이 없다면 break
    if table.get(Now) == None:
        break

    # 현재 위치에서의 움직여야할 방향과 거리를 가져온뒤
    direct, distance = table[Now]

    # 거리에따라 더해줌
    if direct == 'L':
        Now -= distance
    elif direct == 'R':
        Now += distance

print(Now)
