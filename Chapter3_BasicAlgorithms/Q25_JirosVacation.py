ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
B = nl()
ans = (sum(A)+2*sum(B))/3
print(ans)