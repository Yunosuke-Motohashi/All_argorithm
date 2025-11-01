# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cp
# B17 - Frog 1 with Restoration
# Nこの足場がある、i個目の足場の高さはHi
# i+1またはi+2個目の足場にジャンプできる
# iからjまでジャンプする際のコストは|Hi - Hj|
# 足場1から足場Nまで行くときの、最小コストになる経路を一つ出力する

N = int(input())
H = list(map(int, input().split()))
dp = [ 10**9 ] * N
dp[0] = 0 # 足場1にいるときのコストは0
dp[1] = abs(H[1] - H[0]) # 足場2に行くときのコスト
path = [-1] * N # 経路復元用配列 前の足場のインデックスを記録する
path[1] = 0
for i in range(2, N):
    jump1 = dp[i-1] + abs(H[i]-H[i-1]) # i-1からジャンプする場合
    jump2 = dp[i-2] + abs(H[i]-H[i-2]) # i-2からジャンプする場合
    # dp[i] = min(jump1, jump2)
    if jump1 < jump2:
        # i-1からジャンプした場合の方がコストが小さい
        dp[i] = jump1
        path[i] = i-1
    else:
        # i-2からジャンプした場合の方がコストが小さい
        dp[i] = jump2
        path[i] = i-2
# 経路復元
result = []
cur = N-1
while cur != -1:
    result.append(cur+1)
    cur = path[cur]
result.reverse()
print(len(result))
print(*result)
