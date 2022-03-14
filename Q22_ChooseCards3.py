# N 枚のカードがあり、左から i 番目のカードには整数Aiが書かれています。 和が 100000 となる 2 枚のカードの選び方は何通りあるかを求めるプログラムを作成してください。
ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N = ni()
A = nl()
B = [0]*100001
for i in A:
    B[i]+=1

ans = 0
for i in range(50000):
    ans += B[i]*B[100000-i]
ans += B[50000]*(B[50000]-1)//2
print(ans)