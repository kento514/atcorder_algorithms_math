from collections import deque
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        print(i)
        if i != N/i:
            print(int(N/i))

