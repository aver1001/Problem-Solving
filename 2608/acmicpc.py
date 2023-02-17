import sys
sys.stdin = open('input.txt', "r")
'''

큰숫자 ... 작은숫자 순서대로 계산해야함.
작은숫자 큰숫자 의 경우엔 큰숫자 - 작은숫자 해주면 됨
'''

Loma1 = sys.stdin.readline().rstrip()
Loma2 = sys.stdin.readline().rstrip()

LtoA = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    ###########
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

AtoL = {
    '3000': 'MMM',
    '2000': 'MM',
    '1000': 'M',
    '900': 'CM',
    '800': 'DCCC',
    '700': 'DCC',
    '600': 'DC',
    '500': 'D',
    '400': 'CD',
    '300': 'CCC',
    '200': 'CC',
    '100': 'C',
    '90': 'XC',
    '80': 'LXXX',
    '70': 'LXX',
    '60': 'LX',
    '50': 'L',
    '40': 'XL',
    '30': 'XXX',
    '20': 'XX',
    '10': 'X',
    '9': 'IX',
    '8': 'VIII',
    '7': 'VII',
    '6': 'VI',
    '5': 'V',
    '4': 'IV',
    '3': 'III',
    '2': 'II',
    '1': 'I'
}


def LomaToAra(Loma):
    answer = 0
    N = len(Loma)
    pt = 0
    while pt < N:
        if Loma[pt:pt+2] in LtoA:
            answer += LtoA[Loma[pt:pt+2]]
            pt += 2
        else:
            answer += LtoA[Loma[pt]]
            pt += 1
    return answer


def AraToLoma(Ara):
    Ara = str(Ara)
    N = len(Ara)-1
    answer = ''
    for a in Ara:
        if a+'0'*N in AtoL:
            answer += AtoL[a+'0'*N]
        N -= 1
    return answer


print(LomaToAra(Loma1)+LomaToAra(Loma2))
print(AraToLoma(LomaToAra(Loma1)+LomaToAra(Loma2)))
