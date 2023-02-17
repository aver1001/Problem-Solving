import sys
sys.stdin = open('input.txt', "r")

A, B = map(int, sys.stdin.readline().rstrip().split())


def countOne(num):
    num += 1
    # for i in range(num):
    #     print(bin(i)[2:].zfill(5))

    target = 1
    answer = 0
    while (target) <= num:
        oneSet = num // target
        # print('SET : ', oneSet, target)

        # 세트가 짝수일경우
        if oneSet % 2 != 0:
            # 확인 해줘야함
            answer += (oneSet//2)*target + num % target
            # print((oneSet//2)*target + num % target)
        # 세트가 홀수일경우
        else:
            # 확인 안해도됨.
            answer += (oneSet//2)*target
            # print((oneSet//2)*target)
        target = target << 1

        # print(target)
    # print('Answer : ', answer)
    return answer


countOne(A-1)
countOne(B)
print(countOne(B) - countOne(A-1))
