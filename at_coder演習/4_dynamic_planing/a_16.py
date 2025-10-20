# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p
# A16 - Dungeon 1


# 入力
N = int(input())
A = list(map(int, input().split())) # i-1からiへ行くコスト
B = list(map(int, input().split())) # i-2からiへ行くコスト


dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[0] # i=2へはi=1からしか行けない 1から２に行くコストはA[0]
for i in range(3,N+1):
    # 一段前から来る場合
    tmp1 = dp[i-1] + A[i-2]
    # 二段前から来る場合
    tmp2 = dp[i-2] + B[i-3]
    # 2つの候補のうち、より安いコストを記録する
    dp[i] = min(tmp1, tmp2)

print(dp[N])  # ゴールの部屋Nにたどり着く最小コストを出力