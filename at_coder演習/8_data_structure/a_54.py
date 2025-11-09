# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bb
# A54 - Map
# クエリ１: 生徒xの成績がyであると記録
# クエリ２: 生徒xの成績を出力

Q = int(input())
queries = [input().split() for _ in range(Q)]

from collections import defaultdict
score_map = defaultdict(int)
for q in queries:
    if q[0] == "1":
        score_map[q[1]] = int(q[2])
    elif q[0] == "2":
        print(score_map[q[1]])
