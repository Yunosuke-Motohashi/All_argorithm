# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs
# B20 - Edit Distance
# Sに対して以下の３種類の操作が可能
# 1. 1文字の削除
# 2. 1文字の置換
# 3. 適当な位置への1文字の挿入
# 最小何回でTに変換できるか

"""
編集距離（レーベンシュタイン距離）
編集距離とは、ある文字列を別の文字列に変換するために必要な操作回数の最小値のことです。
"""

S = input()
T = input()

# 動的計画法
N = len(S)
M = len(T)
dp = [ [0] * (M+1) for _ in range(N+1)]
"""
S[:i]をT[:j]に変換するための編集距離を dp[i][j] に保存
dp[i][j] の遷移の可能性は以下の通り
1. Sのi文字目とTのj文字目が一致する場合
   s[:i-1]をt[:j-1]に変換するコストと同等なのでその値と
   s[:i]から
2. Sのi文字目とTのj文字目が不一致の場合
   
"""

for i in range(N+1):
    for j in range(M+1):
        if i == 0:
            # Sが空文字の場合、Tのj文字を挿入する必要がある
            dp[i][j] = j
        elif j == 0:
            # Tが空文字の場合、Sのi文字を削除する必要がある
            dp[i][j] = i
        else:
            # 挿入コスト
            # s[:i]をt[:j-1]に変換しているので、t側が1文字増えたので挿入した時のコスト1を足す
            insert_cost = dp[i][j-1] + 1
            # 削除コスト
            # s[:i-1]をt[:j]に変換しているので、s側が1文字増えたので1文字削除した時のコスト1を足す
            delete_cost = dp[i-1][j] + 1
            if S[i-1] == T[j-1]:
                # Sのi文字目とTのj文字目が一致する場合
                # s[:i-1]をt[:j-1]のコストをそのまま引き継ぐ　一致しているため何もしない
                dp[i][j] = min(dp[i-1][j-1], insert_cost, delete_cost)
            else:
                # Sのi文字目とTのj文字目が不一致の場合、置換コストが発生
                # 置換コスト 
                # s[:i-1]をt[:j-1]に変換しているので、互いに1文字ずつ足しているのでそれを置換すれば良い
                replace_cost = dp[i-1][j-1] + 1 
                dp[i][j] = min(replace_cost, insert_cost, delete_cost)
# 出力
print(dp[N][M])