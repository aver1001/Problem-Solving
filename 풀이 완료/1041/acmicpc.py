import sys
sys.stdin = open('input.txt', "r")

N = int(sys.stdin.readline().rstrip())
A,B,C,D,E,F= map(int,sys.stdin.readline().rstrip().split())

one = min(A,B,C,D,E,F)
two = min((A+B),(A+C),(A+D),(A+E),(B+C),(B+D),(D+E),(E+C),(F+B),(F+C),(F+D),(F+E))
three = min((A+B+C),(A+E+C),(A+E+D),(A+D+B),(F+B+D),(F+D+E),(F+E+C),(F+C+B))

if N == 1:
    print(A+B+C+D+E+F -max(A,B,C,D,E,F))
    exit(0)

def calMin(one,two,three):
    return calOne(one) + calTwo(two) + calThree(three)

def calOne(one):
    return one * (4 * (N - 2) * (N - 1) + (N - 2) ** 2)

def calTwo(two):
    return two*(4 * (N - 1) + 4 * (N - 2))

def calThree(three):
    return three*4

print(calMin(one,two,three))