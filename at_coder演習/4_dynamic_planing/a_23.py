# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_w
# A23 - All Free
# N個の商品がある
# M個のクーポンがあり、1の場合は商品iを無料で手に入れられる
# 最小何個のクーポンを使えば、全ての商品を無料で手に入れられるか
"""
集合をビット集合で表す典型的な
ビットマスク DP（動的計画法）問題

"""
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(M)]
INF = 10 ** 9
dp = [[INF] * (2 ** N) for _ in range(M+1)]
# 「先頭 i 枚のクーポンだけを使ったとき、
# 商品集合 s（ビット集合）を無料にできる最小クーポン枚数」を記録

dp[0][0] = 0
for i in range(1, M+1): # クーポンiまでを使う場合
    for j in range(2**N):
        already = [None] * N # already[k] = 1の時、商品kはすでに無料になっている
        for k in range(N):
            # jのkビット目が1か0かで判定
            if (j // 2**k) % 2 == 1:
                already[k] = 1
            else:
                already[k] = 0

        # クーポンiを使う場合の整数表現を計算
        v = 0 # 
        for k in range(N):
            if already[k] == 1 or A[i-1][k] == 1:
                v += 2**k
        # クーポンを使わない場合　状態はそのままなのでj
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        # クーポンを使うと状態はvになる
        dp[i][v] = min(dp[i][v], dp[i-1][j] + 1)

if dp[M][2**N - 1] == INF:
    print(-1)
else:
    print(dp[M][2**N - 1])



"""
無料にできる、できないの仮想状態をビットで表す(状態j)
その状態からクーポンiを利用した場合、
無料で追加できるものが増えるまたは同じになる
dp[i][j]はjの状態になるための現状の最小クーポン枚数を表す
vの状態になるには現状のクーポン数に1を足す（これ以前に最小あればそちらを採用する）
全てを無料にするには全てが１の状態、つまり2**N - 1の状態にする必要がある
"""
