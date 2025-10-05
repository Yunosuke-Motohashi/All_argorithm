# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_o
# A15 - Compression
import bisect

N = int(input())
A_l = list(map(int, input().split()))
# 重複を削除しソートする
T = list(set(A_l))
T.sort()

B = [0] * N
for i in range(N):
    # A_l[i]がTの何番目にあるかを二分探索で調べて、そのTにおけるindexをBに格納
    pos = bisect.bisect_left(T, A_l[i])
    B[i] = pos+1
print(*B)
