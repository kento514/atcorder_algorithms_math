ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
ans = 'First'
for i in range(65):
    if N==2**i -1 :
        ans = 'Second'
        break
print(ans)