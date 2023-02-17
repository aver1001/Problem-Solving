import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
Tree = {}
for _ in range(N):
    cost, left, right = map(int, sys.stdin.readline().rstrip().split(' '))

    if cost in Tree:
        Tree[cost]['left'] = left
        Tree[cost]['right'] = right
    else:
        Tree[cost] = {'mother': None, 'left': left,
                      'right': right, 'colum': -1, 'row': -1}

    if right != -1 and right in Tree:
        Tree[right]['mother'] = cost
    else:
        Tree[right] = {'mother': cost, 'left': left,
                       'right': right, 'colum': -1, 'row': -1}

    if left != -1 and left in Tree:
        Tree[left]['mother'] = cost
    else:
        Tree[left] = {'mother': cost, 'left': left,
                      'right': right, 'colum': -1, 'row': -1}

col = 1
row = 1
rowCol = {}
# left mid right


def findRoot():
    for key, value in Tree.items():
        if value['mother'] == None:
            return key


def round(node, row):
    global col

    if Tree[node]['left'] != -1:
        round(Tree[node]['left'], row+1)

    if row in rowCol:
        rowCol[row]['max'] = max(rowCol[row]['max'], col)
        rowCol[row]['min'] = min(rowCol[row]['min'], col)
    else:
        rowCol[row] = {'max': col, 'min': col}

    Tree[node]['colum'] = col
    col += 1
    Tree[node]['row'] = row

    if Tree[node]['right'] != -1:
        round(Tree[node]['right'], row+1)


round(findRoot(), 1)


answer = [1, 1]
for key in range(1, N):
    if key not in rowCol:
        break
    value = rowCol[key]
    sub = value['max'] - value['min'] + 1
    if answer[1] < sub:
        answer = [key, sub]
print(*answer)
