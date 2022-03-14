ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N,S = na()
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j<=S:
            ans+=1
        else:
            continue
print(ans)
