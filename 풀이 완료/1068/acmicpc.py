import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
tree = list(map(int, sys.stdin.readline().rstrip().split(' ')))
DeleteNode = int(sys.stdin.readline().rstrip())

# 나를 참조하는게 있으면 나는 리프노드가 아님.


def isLeaf(idx):
    try:
        # 리프아님
        tree.index(idx)
        return False
    except:
        # 리프임
        return True


def countLeaf():
    cnt = 0
    for idx in range(N):
        if isLeaf(idx):
            cnt += 1

    return cnt


def deleteNone(target):
    cnt = 0
    # 나를 참조하는 친구들중에 리프인거 찾으면 댐
    if target == 0:
        cnt += 1
    flag = False
    for idx in range(N):
        if tree[idx] == target:
            cnt += deleteNone(idx)
            flag = True
    if flag == False:
        return 1

    return cnt


print(countLeaf()-deleteNone(DeleteNode))
