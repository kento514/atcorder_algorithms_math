import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

n, r = na()
ans = math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
print(ans)



