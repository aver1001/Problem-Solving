import sys
sys.stdin = open('input.txt', "r")

T = int(sys.stdin.readline().strip())


for _ in range(T):
    n = int(sys.stdin.readline().strip())
    trie = {}
    flag = False
    numbers = []
    for _ in range(n):
        numbers.append(sys.stdin.readline().strip())
    numbers.sort()

    for number in numbers:
        temp = trie
        for num in number:
            if num in temp:
                temp = temp[num]
                if 'check' in temp:
                    flag = True
            else:
                temp[num] = {}
                temp = temp[num]
            if flag:
                break
        temp['check'] = 1
        if flag:
            break

    if flag:
        print('NO')
    else:
        print('YES')
