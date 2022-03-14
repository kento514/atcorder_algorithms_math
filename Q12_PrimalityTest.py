ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
x = (N%2!=0)
y = all([(N%k)!=0 for k in range(3,int(N**0.5)+1,2)])
if x and y:
    print('Yes')
else:
    print('No')
