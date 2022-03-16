import math
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
Ns = {1:0,2:0, 3:0}
for i in A:
    Ns[i]+=1
ans = 0
for key in Ns.keys():
    ans += Ns[key]*(Ns[key]-1)//2
print(ans)