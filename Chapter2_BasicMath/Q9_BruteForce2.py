ni = lambda: int(input())
nl = lambda: list(map(int, input().split()))
na = lambda: map(int,input().split())
ns = lambda: input()

N,S = na()
A = nl()
def find_max_dp(num_list):
    dp_table = [[0 for _ in range(S + 1)] for i in range(N)]
 
    # 1番目のカード
    for j in range(S + 1):
        if num_list[0] <= j:
            dp_table[0][j] = num_list[0] # 1番目のカードを追加
 
    # 2番目以降のカード
    for i in range(N):
        for j in range(S + 1):
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j: # コスト不足のとき
                dp_table[i][j] = tmp_not_choice 
            else:
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
 
    return dp_table[N - 1][S]
 
if find_max_dp(A)==S:
    print('Yes')
else:
    print('No')
