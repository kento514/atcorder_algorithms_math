ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

a, b = na()
mod = 1000000007
p = a
ans = 1
for i in range(31):
    if b & 1<<i:
        ans = (ans*p)%mod
    p = (p*p)%mod
print(ans)