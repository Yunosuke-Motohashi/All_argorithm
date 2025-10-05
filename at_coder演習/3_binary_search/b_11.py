# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj
# B11 - Binary Search 2

import bisect

N = int(input())
A_l = list(map(int, input().split()))
A_l.sort()
Q = int(input())
for _ in range(Q):
    X = int(input())
    # A_lの中でX以上となる最小のindexを二分探索で調べる
    # そのindex以下の値は全てX以下未満となる
    pos = bisect.bisect_left(A_l,X)
    print(pos)


"""
# copilot質問メモ
Q. bisect_leftとbisect_rightの違いは？

A. 
bisect_left と bisect_right の違い:

・bisect_left(a, x): x を挿入して順序を保つ最左位置（既に x があればその最初の位置）を返す 条件: a[:pos] < x <= a[pos:]
・bisect_right(a, x) / bisect.bisect(a, x): x を挿入して順序を保つ最右位置（既に x があればその最後の直後）を返す 条件: a[:pos] <= x < a[pos:]

例: a = [1, 2, 2, 4] bisect_left(a, 2) -> 1 (最初の 2 の位置) bisect_right(a, 2) -> 3 (最後の 2 の次の位置)

応用:
・値 x の出現回数: bisect_right(a, x) - bisect_left(a, x)
・x 以上の要素数: len(a) - bisect_left(a, x)
・x 以下の要素数: bisect_right(a, x)
計算量はどちらも O(log N) (比較回数は二分探索) です。
"""