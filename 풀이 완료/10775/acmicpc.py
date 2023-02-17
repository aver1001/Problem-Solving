import sys
sys.stdin = open('input.txt', "r")

G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

Gate = [i for i in range(G+1)]
isFull = [False]*(G+1)


def findGate(num):
    if num == 0:
        return -1

    if Gate[num] == num:
        Gate[num] -= 1
        return num
    else:
        temp = findGate(Gate[num])
        Gate[num] = temp
        return temp


answer = 0
for _ in range(P):
    airplane = int(sys.stdin.readline().rstrip())

    if isFull[airplane] == False:
        isFull[airplane] = True
        Gate[airplane] -= 1
    else:
        temp = findGate(airplane)
        if temp == -1:
            break
        isFull[temp] = True
    answer += 1

print(answer)
