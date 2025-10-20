# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q
# A17 - Dungeon 2
N = int(input())
A = list(map(int, input().split())) # i-1からiへ行くコスト
B = list(map(int, input().split())) # i-2からiへ行くコスト

dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[0] # i=2へはi=1から
path = [0] * (N+1) # i番目の部屋に来る直前の部屋番号
path[2] = 1
for i in range(3,N+1):
    # 一段前から来る場合
    tmp1 = dp[i-1] + A[i-2]
    # 二段前から来る場合
    tmp2 = dp[i-2] + B[i-3]
    if tmp1 < tmp2:
        # 一段前から来る方が安い場合
        dp[i] = tmp1
        path[i] = i-1
    else:
        # 二段前から来る方が安い場合
        dp[i] = tmp2
        path[i] = i-2

# 経路復元
ans = []
j = N
while j > 0:
    ans.append(j)
    j = path[j]
print(len(ans))
# 部屋の通過順を出力
print(*ans[::-1])