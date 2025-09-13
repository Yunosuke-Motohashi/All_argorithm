# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i
# A09 - Winter in ALGO Kingdom 

# 2次元いもす法で解く -> h * wを h+2 * w+2に拡張しないと、(h, w)などの最大値の処理ができない
h, w, n = map(int, input().split())
area = [[0] * (w+2) for _ in range(h+2)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    area[a][b] += 1
    area[a][d+1] -= 1
    area[c+1][d+1] += 1
    area[c+1][b] -= 1
# 横方向の累積和
for i in range(h+1):
    for j in range(1, w+1):
        area[i][j] += area[i][j-1]
# 縦方向の累積和
for j in range(w+1):
    for i in range(1, h+1):
        area[i][j] += area[i-1][j]
for a in area:
    print(*a)