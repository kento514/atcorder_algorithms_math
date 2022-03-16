ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

T = ni()
N = ni()
Num = [0]*(T+1)
for _ in range(N):
    L, R = na()
    Num[L]+=1
    Num[R]-=1

ans = 0
for i in range(T):
    ans += Num[i]
    print(ans)