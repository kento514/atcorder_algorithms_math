import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
Ns = {100:0,200:0, 300:0, 400:0}
for i in A:
    Ns[i]+=1

print(Ns[100]*Ns[400]+Ns[200]*Ns[300])