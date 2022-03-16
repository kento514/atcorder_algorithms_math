ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
mod = 1000000007
ans = [0]*N
ans[0] = 1
ans[1] = 1
for i in range(N-2):
    ans[i+2] = (ans[i] + ans[i+1])%mod

print(ans[-1])