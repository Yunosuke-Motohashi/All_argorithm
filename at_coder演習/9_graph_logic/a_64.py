# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bl
# A64 - Shortest Path 2
# N, M = map(int, input().split())
# graph = [list() for _ in range(N+1)]
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# 幅優先探索
# from collections import deque
# cost = [-1] * (N + 1) # 各頂点までのコスト、-1は未訪問 -1とするのはコストが0のときの場合もあり得るため
# cost[1] = 0 # 頂点1までのコストは0
# Q = deque() # BFS用のキュー
# Q.append(1) # 頂点1から探索開始

# while Q: # キューが空になるまで繰り返す
#     pos = Q.popleft() # キューから先頭を取り出す
#     for next in graph[pos]:
#         next_v, next_c = next
#         if cost[next_v] == -1:
#             cost[next_v] = cost[pos] + next_c
#             Q.append(next_v)
#         else:
#             continue
# # 結果の出力
# for i in range(1, N+1):
#     print(cost[i])



N, M = map(int, input().split())
# 重み付き無向グラフ
graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# ダイクストラ法
# ダイクストラ法は、グラフ理論における重みが非負の「単一始点最短経路問題」を解くためのアルゴリズムです。
# ある始点から他のすべての頂点への最短経路を効率的に見つけ出すことができます。
import heapq
INF = 10**10 # 十分大きな値
current = [INF] * (N + 1) # 始点(頂点1)から各頂点への 現時点での最短距離の暫定値（テンティティブ距離）を格納。 INFは未訪問
current[1] = 0 # 頂点1までのコストは0
Q = [] # 優先度付きキュー
# heapqは常に最小要素が先頭に来るように管理されている
# (コスト, 頂点)の順で格納
# コストが小さい順に取り出される
heapq.heappush(Q, (current[1], 1))

kakutei = [False] * (N + 1) # 各頂点が確定済みかどうか

while Q: # キューが空になるまで繰り返す
    # 次に、確定するべき頂点を求める
    # ここでは、優先度付きキューの最小要素を取り出す
    cost, pos = heapq.heappop(Q) # キューから最小要素を取り出す
    if kakutei[pos]: # 既に確定済みならスルー
        continue
    kakutei[pos] = True # 頂点posを確定済みにする
    for next in graph[pos]: # posに隣接する頂点を調べる
        # print(pos, next, current, Q)
        next_pos, next_c = next
        if current[next_pos] > current[pos] + next_c:
            # next_posでcurrent[next_pos]よりも小さいコストで到達できる場合
            current[next_pos] = current[pos] + next_c
            heapq.heappush(Q, (current[next_pos], next_pos )) # 現在のコストを優先度付きキューに追加
    # print(kakutei[1:])
    # print(current[1:])


for ans in current[1:]:
    if ans != INF:
        print(ans)
    else:
        print(-1)
