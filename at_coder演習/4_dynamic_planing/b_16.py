# https://atcoder.jp/contests/tessoku-book/tasks/dp_a
# B16 - Frog 1
# Nこの足場がある、i個目の足場の高さはHi
# i+1またはi+2個目の足場にジャンプできる
# iからjまでジャンプする際のコストは|Hi - Hj|
# 足場1から足場Nまで行くときの、最小コスト

N = int(input())
H = list(map(int, input().split()))

dp = [ 10**9 ] * N
dp[0] = 0 # 足場1にいるときのコストは0
dp[1] = abs(H[1] - H[0]) # 足場2に行くときのコスト
for i in range(2, N):
    jump1 = dp[i-1] + abs(H[i]-H[i-1]) # i-1からジャンプする場合
    jump2 = dp[i-2] + abs(H[i]-H[i-2]) # i-2からジャンプする場合
    dp[i] = min(jump1, jump2)

print(dp[N-1])
