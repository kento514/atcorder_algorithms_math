import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, X, Y = na()
Z = X*Y//math.gcd(X, Y)
print((N//X)+(N//Y)-(N//Z))
