ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

a, b = na()
X = (2*a-b)/3
Y = (-a+2*b)/3
if (X-int(X)==0) and (Y-int(Y)==0):
    mod = 1000000007
    X = int(X)
    Y = int(Y)
    def cmb(n, r, mod):
        if ( r<0 or r>n ):
            return 0
        return g1[n] * g2[r] * g2[n-r] % mod

    N = X+Y
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    a = cmb(N,min(X,Y),mod)
    print(a)
else:
    print(0)