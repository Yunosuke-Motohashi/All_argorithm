# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r
# A18 - Subset Sum
# 合計が S になるような部分集合が存在するかどうかを判定する問題

N, S = map(int, input().split())
A = list(map(int, input().split()))

# DPでA[i]を使う場合、使わない場合で取りうる値を管理する
# dp[i] : Aの先頭i個までを使って作れる和のパターン　jが作れるか作れないか(作れる場合はTrue、作れない場合はFalse)

dp = [ [None] * (S+1) for _ in range(N+1)]
# dp i=0
dp[0][0] = True # 何も選ばない場合、和0は作れる
for i in range(1, S+1):
    dp[0][i] = False # 何も選ばない場合、和i (i>0)は作れない

# dp i>=1
for i in range(1, N+1): # Aの先頭i個までをいくつか使う場合
    for j in range(S+1): # 和jが作れるかどうか
        if j < A[i-1]: # A[i-1]以下の場合、A[i-1]は使わないので、前の状態を引き継ぐ
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if j >= A[i-1]: # A[i-1]を使う場合、使わない場合の両方を考慮する
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                # dp[i-1][j] == True: A[i-1]を使わない場合で和jが作れる
                # dp[i-1][j-A[i-1]] == True: j-A[i-1]がTrueである場合は、そこにA[i-1]を足しても和jが作れることになりTrue
                dp[i][j] = True
            else:
                dp[i][j] = False
# 最終的に和Sが作れるかどうか
if dp[N][S] == True:
    print("Yes")
else:
    print("No")