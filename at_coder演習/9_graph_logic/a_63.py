# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_an
# A63 - Shortest Path 1

N, M = map(int, input().split())

graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 幅優先探索(BFS)の準備
from collections import deque
distance = [-1] * (N+1) # 各頂点までの距離、-1は未訪問 -1とするのは距離が0のときの場合もあり得るため
distance[1] = 0 # 頂点1までの距離は0
Q = deque() # BFS用のキュー
Q.append(1) # 頂点1から探索開始

# 幅優先探索(BFS)
while Q: # キューが空になるまで繰り返す
    pos = Q.popleft() # キューから先頭を取り出す
    for next in graph[pos]: # posに隣接する頂点を調べる
        if distance[next] == -1: # 隣接する頂点が未訪問の場合
            distance[next] = distance[pos] + 1 # 隣接する頂点までの距離を更新
            Q.append(next) # キューに追加する
        else:
            # BFSでは最初に訪れたときが最短距離なので、
            # 既に訪問済みなら何もしない
            continue

# 結果の出力
for i in range(1, N+1):
    print(distance[i])
