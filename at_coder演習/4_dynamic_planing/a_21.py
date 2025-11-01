# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u
# A21 - Block Game
# N個のブロック
# 右から取り除くか、左から取り除くかを選ぶことができる
# ブロックiをPiより先に取り除いた時に得られる得点はAi
# 合計得点の最大値を求める問題

N = int(input())
P = [None] * (N+1)
A = [None] * (N+1)
for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())

dp = [ [None]*(N+1) for _ in range(N+1)]
dp[1][N] = 0 # 初期状態(全部残ってるとき)の得点は0
for LEN in reversed(range(0, N-1)):
    # LENは残すブロックの長さ lからrまでを残す
    for l in range(1, N-LEN+1): # lの最大値はrを超えないためN-LEN
        r = l + LEN # rは右端のブロックの位置なので、lに長さLENを足す

        # 左から取る(l-1番目のブロックを取り除く)場合の得点
        score_l = 0
        if l>=2 and l <= P[l-1] and P[l-1] <= r:
            # l-1番目を取る場合、lからrの間にP[l-1]があるときに
            # つまり、ブロックl-1をブロックP[l-1]よりも先に取り除けるので、得点A[l-1]が加算される
            score_l = A[l-1]
        # 右から取る場合の得点
        score_r = 0
        if r<=N-1 and l<=P[r+1] and P[r+1]<=r:
            # r+1番目を取る場合、lからrの間にP[r+1]があるときに
            # つまり、ブロックr+1をブロックP[r+1]よりも先に取り除けるので、得点A[r+1]が加算される
            score_r = A[r+1]

        # dp[l][r]: ブロックlからrまでが残っているときの最大得点
        if l == 1:
            # 左端が1のとき、右から取る
            # 外側の点数に右から取る場合の得点を足す
            dp[l][r] = dp[l][r+1] + score_r
        elif r == N:
            # 右端がNのとき、左から取る
            # 外側の点数に左から取る場合の得点を足す
            dp[l][r] =  dp[l-1][r] + score_l
        else:
            # 左右両方から取れるとき、どちらか得点が大きい方を採用する
            dp[l][r] = max(dp[l-1][r] + score_l, dp[l][r+1] + score_r)

# dpはi=jの時、
# つまり1個のブロックが残っているときの得点が最終的な答えになる
ans = 0
for i in range(1, N+1):
    ans = max(ans, dp[i][i])
print(ans)

"""入力例
4
4 20
3 30
2 40
1 10

dpの中身
[None, None, None, None, None]
[None, 50, 50, 10, 0]
[None, None, 60, 20, 20]
[None, None, None, 50, 50]
[None, None, None, None, 50]
答え: 60
"""