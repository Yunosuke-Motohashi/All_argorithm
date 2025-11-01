# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq
# B18 - Subset Sum with Restoration 
# N枚のカードからいくつかを選んで、その和がSになるようにしたい。
# そのような選び方が存在するかを判定し、存在する場合にはその一例を出力せよ。

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None] * (S + 1) for _ in range(N + 1)] # dp[i][j]: Aの先頭i個までを使って和jが作れるかどうか
dp[0][0] = True # 何も選ばない
for i in range(1, S+1):
    dp[0][i] = False

for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i-1]: # A[i-1]以下の場合、A[i-1]は使わないので、前の状態を引き継ぐ
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else: #j >= A[i-1]でA[i-1]を使う場合
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                # dp[i-1][j] == True: もうすでに和jが作れる場合
                # dp[i-1][j-A[i-1]] == True: j-A[i-1]がTrueである場合は、
                # そこにA[i-1]を足しても和jが作れることになりTrue
                dp[i][j] = True
            else:
                dp[i][j] = False
# 選び方が存在しない場合
if dp[N][S] == False:
    print(-1)
    exit()

# 選び方が存在する場合、復元
# 和がSになるようなAのインデックスを復元する
result = []
cur_s = S
for i in reversed(range(1,N+1)):
    if dp[i-1][cur_s] == True:
        # i-1まででcur_sが作れる場合、A[i]は使っていない
        continue
    else:
        # dp[i-1][cur_s] == False
        # 基本的にdp[i][cur_s] == Trueであるはずなので、A[i]は使っている
        result.append(i)
        cur_s -= A[i-1]
print(len(result))
print(*reversed(result))

