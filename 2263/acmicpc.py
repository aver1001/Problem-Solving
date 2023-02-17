import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt', "r")
'''
preOrder    전위순회    나 왼쪽 오른쪽
inOrder     중위순회    왼쪽 나 오른쪽
postOrder   후위순회    왼쪽 오른쪽 나
'''

N = int(sys.stdin.readline().rstrip())

inOrder = list(map(int, sys.stdin.readline().rstrip().split(' ')))
postOrder = list(map(int, sys.stdin.readline().rstrip().split(' ')))
nodeNum = [0] * (N + 1)
for i in range(N):
    nodeNum[inOrder[i]] = i


def findTree(preLt, preRt, inLt, inRt):
    if (inLt > inRt) or (preLt > preRt):
        return

    # 후위순회에서 root를 찾아준다.
    root = postOrder[preRt]

    leftNode = nodeNum[root] - inLt
    rightNode = inRt - nodeNum[root]
    print(root, end=' ')
    findTree(preLt, preLt+leftNode-1, inLt, inLt+leftNode-1)
    findTree(preRt-rightNode, preRt-1, inRt-rightNode+1, inRt)


findTree(0, N-1, 0, N-1)
print()
print(nodeNum)
print(postOrder)
print(inOrder)
