# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_v
# A22 - Sugoroku
# N個のマスがある双六で、２種類の行動を取れる
# Aiマスに進むと100点
# Biマスに進むと150点
# Nマスに到達したときの最大得点を求める問題
# Aiに行くかBiに行くか決めることができる

# 前方型 DP（一次元 DP・経路最適化）問題

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-10 ** 9] * (N+1)
# 十分小さい -10**9 にしておかないと、更新式正値へ跳ね上がり、あり得ない経路が生まれ、
# 未到達マスは更新後も大きく負のままなので誤って到達扱いになることはない
dp[1] = 0 # 初期値 1からスタートするので0点
for i in range(1, N):
    # i から A[i-1], B[i-1] に進む場合、得点が大きい方を採用
    a = A[i-1]
    b = B[i-1]
    dp[a] = max(dp[a], dp[i]+100)
    dp[b] = max(dp[b], dp[i]+150)

print(dp[N])