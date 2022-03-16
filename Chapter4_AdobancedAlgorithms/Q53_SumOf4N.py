ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
mod = 1000000007
ans = ((pow(4,N+1,mod)-1)*pow(3,-1,mod))%mod
print(ans)