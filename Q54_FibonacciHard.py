import numpy as np
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

n = ni() -1
mod = 10**9
A = np.array([[1,1],[1,0]])
fib = [A]

for i in range(1,70):
    fib.append(np.dot(fib[i-1],fib[i-1])%mod)

ans = np.array([[1,0],[0,1]])
for i in range(70):
    if n>>i & 1 != 0:
        ans = np.dot(ans, fib[i])%mod

print(ans[0][0])