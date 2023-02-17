import sys
from collections import deque
sys.stdin = open('input.txt', "r")

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

isRight = True


def DFS(string, isRight):

    if len(string) == len(B):
        if string == B:
            print(1)
            exit()
        return

    if isRight:
        DFS(string+'A', isRight)
        DFS('B'+string, not(isRight))
    else:
        DFS('A'+string, isRight)
        DFS(string+'B', not(isRight))


DFS(A, True)
print(0)
