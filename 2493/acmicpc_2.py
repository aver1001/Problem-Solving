import sys
sys.stdin = open('input.txt', "r")
'''
일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽방향으로 차례로 세우고
각 탑의 꼭대기에 레이저 송신기를 설치하였다.

모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽방향으로 발사하고
탑의 기둥 모두에는 레이저를 수신하는 장치가 설치되어 있다.
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다

탑들의 개수 N과 탑들의 높이가 주어질떄, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라

주어진 탑들의 순서대로 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들이 번호를 하나의 빈칸을 사이에 두고 출력한다
만약 레이저 신호를 수신하는 탑이 존재하지 않으면 0을 출력한다
'''

'''
결국 오른쪽부터 확인했을때 자신보다 큰게 나오면 되는것

하나씩 pop 해줘서 스택을 쌓아간다.
스택에 가장 아랫부분의 수보다 큰 수가 들어올경우 다 뺴서 지금 인덱스의 번호를 정리해서 넣어준다
스택에 가장 아랫부분의 수보다 작은 수가 들어올경우 그냥 넣어준다.
'''

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
result = [0]*N

for i in range(1, N):
    target = i-1
    print('target', target)
    print(result)
    while target != -1:
        if arr[target] >= arr[i]:
            result[i] = target+1
            break
        else:
            target = result[target]-1
        print(target)

print(*result)
