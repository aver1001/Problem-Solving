import sys
sys.stdin = open('input.txt', "r")
'''
생일을 맞이한 주성이가 생일파티를 준비한다.
주성이는 일반 케이크 대신 롤케이크를 준비했다.
롤케이크는 장식이 존재해서 특정 위치에서만 자를 수 있다.
주성이는 롤 케이크 조각을 파티에 올 친구의 수 만큼 준비하고 싶어서, 가장 작은 조각의 크기를 미리 알아보리고 했다
하지만 짓궂은 주성이의 친구들은 생일파티에 몇 명이 참석하는지 직접적으로 알려주지를 않는다.
그래서 몇개의 수를 목록에 적어, 각 수 만큼 조각을 만들었을때 가장 작은 조각의 길이의 최댓값을 구하려고 한다.

result
15
10

'''
def is_minimum(mini):
    left = 0
    cnt = 0
    for right in cut_points:
        if right - left >= mini:
            left = right
            cnt += 1
    if cnt > k:
        return True
    return False


N, M, L = map(int, input().split())
cut_points = [int(input()) for _ in range(M)] + [L]
print(N,M,L)
print(cut_points)
for _ in range(N):
    k = int(input())
    # M개의 지점 중 k개 선택. 사잇값의 최솟값이 가장 큰.
    left = 1
    right = 4000000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if is_minimum(mid):
            left = mid + 1
            answer = max(mid,answer)
        else:
            right = mid - 1
    print(answer)