# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
# A08 - Two Dimensional Sum
h, w = map(int, input().split())
x_l = []
sums = [[0] * (w+1) for _ in range(h+1)]
for i in range(h):
    row = list(map(int, input().split()))
    x_l.append(row)
    # 横方向の累積和
    for j in range(w):
        if j==0:
            sums[i+1][j+1] = row[j]
        else:
            sums[i+1][j+1] = sums[i+1][j] + row[j]
# 縦方向の累積和
for i in range(h):
    if i == 0:
        continue
    for j in range(w):
        sums[i+1][j+1] += sums[i][j+1]

# print(*sums, sep="\n")
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ans = sums[c][d] - sums[a-1][d] - sums[c][b-1] + sums[a-1][b-1] #引き過ぎ分を足す
    print(ans)
