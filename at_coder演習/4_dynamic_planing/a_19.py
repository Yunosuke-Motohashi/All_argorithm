# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s
# A19 - Knapsack 1

N, W = map(int, input().split())

w = [None] * (N+1)
v = [None] * (N+1)
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

dp = [[-10 ** 9] * (W+1) for _ in range(N+1)]
# 宝石iを選ぶか選ばないか
# dp[i]はweight分の長さを持ち、j番目は重さjのときの価値の最大値を表す
# dp[i][j]: i番目までの宝石を見たときに、重さjで得られる価値の最大値
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(W+1):
        if j < w[i]: 
            # 今見ている重さが宝石iの重さより小さい場合、宝石iは選べない
            dp[i][j] = dp[i-1][j] # 前の状態(i-1)を引き継ぐ
        else:
            # 宝石iを選ぶ場合
            # j-w[i]の重さつまり、宝石i-1を見た時の最大価値にv[i]を足したものと
            # 宝石iを選ばない場合の価値dp[i-1][j]を比較して大きい方を採用する
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
# dp[N]の中で最大のものが答え
print(max(dp[N]))