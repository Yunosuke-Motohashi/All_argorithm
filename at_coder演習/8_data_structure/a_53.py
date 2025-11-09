# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ba
# A53 - Priority Queue
# クエリ１: x円の表品を追加
# クエリ２: キューの中で最安値の商品の価格を出力
# クエリ３: キューの中の最安値の商品を削除

Q = int(input())
queries = [input().split() for _ in range(Q)]

import heapq
pq = [] # 優先度付きキューの初期化

for q in queries:
    if q[0] == "1":
        heapq.heappush(pq, int(q[1]))
    elif q[0] == "2":
        print(pq[0])
    else: # q[0] == 3
        heapq.heappop(pq)  # キューから最小要素を取り出す
