# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg
# B08 - Counting Points
N = int(input())
lim = 1500
xy = [[0] * (lim + 1) for _ in range(lim + 1)]
for _ in range(N):
    x, y = map(int, input().split())
    xy[x][y] += 1

# 横方向の累積和
for i in range(lim + 1):
    for j in range(1, lim + 1):
        xy[i][j] += xy[i][j-1]

# 縦方向の累積和
for i in range(1, lim + 1):
    for j in range(lim + 1):
        xy[i][j] += xy[i-1][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    ans = xy[c][d] - xy[c][b-1] - xy[a-1][d] + xy[a-1][b-1]
    print(ans)
