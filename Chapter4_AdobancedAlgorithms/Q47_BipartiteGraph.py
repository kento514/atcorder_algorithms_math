from collections import deque
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, M = na()
G = [list() for _ in range(N)]
for _ in range(M):
    A, B = na()
    G[A-1].append(B-1)
    G[B-1].append(A-1)

c = [0]*N



for i in range(N):
    if c[i] != 0:
        continue
    q = deque([i])
    c[i] = 1
    while q:
        x = q.pop()
        for i in G[x]:
            if c[i]==0:
                c[i]=c[x]*(-1)
                q.append(i)
            elif c[i]==c[x]:
                print('No')
                exit()
print('Yes')