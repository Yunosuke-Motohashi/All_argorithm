# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ch
# B09 - Papers
n = int(input())
lim = 1500
papers = [[0] * (lim +2) for _ in range(lim +2)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    # 座標の場合、枠内が面積になるようにする
    papers[a][b] += 1
    papers[c][d] += 1
    papers[a][d] -= 1
    papers[c][b] -= 1
# 横方向の累積和
for i in range(lim + 2):
    for j in range(1, lim + 2):
        papers[i][j] += papers[i][j - 1]
# 縦方向の累積和
for j in range(lim + 2):
    for i in range(1, lim + 2):
        papers[i][j] += papers[i - 1][j]

# 1以上の箇所をカウント
ans = 0
for i in range(lim + 1):
    for j in range(lim + 1):
        if papers[i][j] > 0:
            ans += 1
print(ans)
