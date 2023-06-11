import sys
sys.setrecursionlimit(9999999)
sys.stdin = open('input.txt', "r")

def makeBinarySearchTree(numbers):
    #첫 숫자를 root로 넣어주고
    BST = {numbers[0]:[0,0]}
    #하나씩 이진트리에 넣어준다
    for num in numbers[1:]:
        insertToTree(BST,numbers[0],num)
    #만들어진 이진트리 리턴
    return BST

def insertToTree(BST,nowNum,insertNum):
    #지금 숫자보다 넣을 숫자가 클경우
    if insertNum > nowNum:
        #나보다 오른쪽으로 가야함
        #만약 오른쪽이 비어있다면
        if BST[nowNum][1] == 0:
            #지금 숫자로 넣어주고
            BST[nowNum][1] = insertNum
            #방금 넣은숫자의 왼쪽오른쪽을 초기화 해준다
            BST[insertNum] = [0,0]
        #비어있지 않다면
        else:
            #오른쪽으로 가서 재귀적으로 실행한다
            insertToTree(BST,BST[nowNum][1],insertNum)
        
    #지금 숫자보다 넣을 숫자가 작은경우
    else:
        #나보다 왼쪽으로 가야함
        #만약 왼쪽이 비어있다면
        if BST[nowNum][0] == 0:
            #지금 숫자로 넣어주고
            BST[nowNum][0] = insertNum
            #방금 넣은 숫자의 왼쪽 오른쪽을 초기화 해준다
            BST[insertNum] = [0,0]
        #비어있지 않다면
        else:
            #왼쪽으로 가서 재귀적으로 실행한다.
            insertToTree(BST,BST[nowNum][0],insertNum)

def postorder(BST,num):
    
    #왼쪽
    if BST[num][0] != 0:
        postorder(BST,BST[num][0])
    #오른쪽
    if BST[num][1] != 0:
        postorder(BST,BST[num][1])
    #루트
    print(num)

numbers = []
while True:
    try:
        numbers.append(int(sys.stdin.readline().rstrip()))
    except:
        break

postorder(makeBinarySearchTree(numbers),numbers[0])