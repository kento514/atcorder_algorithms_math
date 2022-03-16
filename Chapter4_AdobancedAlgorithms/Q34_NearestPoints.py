ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
xy = [nl() for _ in range(N)]
ans = 10**18
def distance(x1, x2):
    return ((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)**0.5

for i in range(N-1):
    for j in range(i+1,N):
        ans = min(ans, distance(xy[i], xy[j]))

print(ans)