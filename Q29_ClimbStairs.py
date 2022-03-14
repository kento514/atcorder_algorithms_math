ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
ans = [0]*(N+1)
ans[0]=1
ans[1]=1
for i in range(N-1):
    ans[i+2] = ans[i+1]+ans[i]
print(ans[-1])