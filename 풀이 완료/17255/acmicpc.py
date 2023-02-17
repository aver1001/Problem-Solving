import sys
sys.stdin = open('input.txt', "r")

N = sys.stdin.readline().rstrip()

lenN = len(N)
answer = set()


def DFS(start, end, string):
    if start == 0 and end == lenN-1:
        answer.add(string)
        return
    if start > 0:
        DFS(start-1, end, string+N[start-1:end+1])
    if end < lenN:
        DFS(start, end+1, string+N[start:end+2])


for start in range(lenN):
    DFS(start, start, N[start])

print(len(answer))
