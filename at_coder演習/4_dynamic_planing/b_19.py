# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr
# B19 - Knapsack 2
# N個の宝石があり、各宝石には重さと価値がある
# 宝石iの重さがw[i]、価値がv[i]
# 重さの総和がWを超えないように宝石を選ぶとき、
# 価値の総和の最大値を求める問題

# a_19.pyのコードだとMLEになる
# 重さの最大値が10**9と大きいため


N, W = map(int, input().split())
w = [None] * (N+1)
v = [None] * (N+1)
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

# dpを価値を基準にする
# vの入力最大値が1000, Nの最大値が100であるため、dpのサイズは1000×100+1にする
# dp[i][j]: i番目までの宝石を見たときに、価値jで得られる重さの最小値
# したがって、dp[N]でW以下のものの中で最大の価値jを探せばよい
dp = [[ 10 ** 15] * 100001 for _ in range(N+1)]
dp[0][0] = 0 # 宝石0個で価値0のときの重さは0

for i in range(1, N+1):
    for j in range(100001):
        if j < v[i]: 
            # 今見ている価値が宝石iの価値より小さい場合、宝石iは選べない
            dp[i][j] = dp[i-1][j] # 前の状態(i-1)を引き継ぐ
        else:
            # 宝石iを選ぶ場合
            # j-v[i]の価値つまり、宝石i-1を見た時の最小重さにw[i]を足したものと
            # 宝石iを選ばない場合の重さdp[i-1][j]を比較して小さい方を採用する
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i]]+ w[i])

# dp[N]の中で重さがW以下で最大価値jが答え
ans = 0
for j in range(100001):
    if dp[N][j] <= W:
        ans = max(ans, j)
print(ans)


"""
重さが大きいため、価値の総和でDPを作る
dp[i][j]: i番目までの宝石を見たときに、価値jで得られる重さの最小値
"""