import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
ans = A[0]
for i in range(1,N):
    ans = ans*A[i]//math.gcd(ans,A[i])
print(ans)