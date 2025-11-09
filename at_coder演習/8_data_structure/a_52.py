# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_az
# A52 - Queue
# クエリ１: xはキューの末尾に追加
# クエリ２: キューの先頭を出力
# クエリ３: キューの先頭を削除

Q = int(input())
queries = [input().split() for _ in range(Q)]

from collections import deque
queue = deque()

for q in queries:
    if q[0] == "1":
        queue.append(q[1])
    elif q[0] == "2":
        print(queue[0])
    else: # q[0] == 3
        queue.popleft()
