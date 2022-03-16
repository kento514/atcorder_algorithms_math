ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, Q = na()
ans = [0]*(N+1)
for _ in range(Q):
    L, R, X = na()
    ans[L-1]+=X
    ans[R]-=X
ans2 = ''
for diff in ans[1:-1]:
    if diff > 0:
        ans2+='<'
    elif diff == 0:
        ans2+='='
    else:
        ans2+='>'
print(ans2)