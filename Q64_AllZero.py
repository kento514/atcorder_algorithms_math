ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N, K = na()
A = nl()
x = sum(A)
if x-K<=0 and (x-K)%2==0:
    print('Yes')
else:
    print('No')