ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
B = nl()
R = nl()

print((sum(B)+sum(R))/N)