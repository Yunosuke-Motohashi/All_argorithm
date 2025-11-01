# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_x
# A24 - LIS
"""
最長増加部分列
与えられた数列から、元の順序を保ったまま要素を抜き出して作られる、
増加する部分列の中で最も長いものです
"""

N = int(input())
A = list(map(int, input().split()))

LEN = 0
L = []
dp = [ None ] * N 

import bisect
for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    dp[i] = pos

    if dp[i] >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[dp[i]] = A[i]
print(LEN)


"""
前からAを見ていき、
LにA[i]が入る位置を二分探索で求める
入る位置とLENを比較し、
LENよりも大きければ、まだLに追加できるので、追加し、LENを1増やす
LEN以下であれば、すでに同じ長さの列があるが、末尾を小さい値で置き換えられる
Lのその位置をA[i]で更新する
"""