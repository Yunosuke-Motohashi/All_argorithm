# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bc
# A55 - Set
# クエリ1：x と書かれたカードが机に置かれる。
# クエリ2：x と書かれたカードが机から除去される。
# クエリ3：机にある x 以上のカードのうち最小のものを答える。

Q = int(input())
queries = [input().split() for _ in range(Q)]

import bisect
cards = []
for q in queries:
    x = int(q[1])
    pos = bisect.bisect_left(cards, x)
    if q[0] == "1":
        cards.insert(pos, x)
    elif q[0] == "2":
        cards.pop(pos)
    else: # q[0] == 3
        if pos == len(cards):
            print(-1)
        else:
            print(cards[pos])
