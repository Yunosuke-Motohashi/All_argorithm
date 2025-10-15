# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ek
# B64 - Shortest Path with Restoration
# 1 -> Nへの最短経路を求める


N, M = map(int, input().split())
# 重み付き無向グラフ
graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


# ダイクストラ + DFSで経路出力は可能だが、記述量が多くなる
# また、MLE (メモリ制限超過) になる
import heapq
INF = 10**10 # 十分大きな値
cost = [INF] * (N + 1) # 始点(頂点1)から各頂点への 現時点での最短距離の暫定値（テンティティブ距離）を格納。 INFは未訪問
cost[1] = 0 # 頂点1までのコストは0
Q = [] # 優先度付きキュー
heapq.heappush(Q, (cost[1], 1))
while Q: # キューが空になるまで繰り返す
    c, pos = heapq.heappop(Q) # キューから最小要素を取り出す
    if cost[pos] != c: # 既に確定済みならスルー
        continue
    if pos == N: # Nに到達したら終了
        break
    for next in graph[pos]: # posに隣接する頂点を調べる
        next_pos, next_c = next
        if cost[next_pos] > cost[pos] + next_c:
            cost[next_pos] = cost[pos] + next_c
            heapq.heappush(Q, (cost[next_pos], next_pos))

# DFSで経路復元
import sys
sys.setrecursionlimit(10**6)
path = [1] # 経路 (頂点1から開始)
visited = [False] * (N + 1) # 各頂点の訪問済みフラグ
def dfs(i: int):
    if i == N:
        print(*path)
        exit()
    for to, c in graph[i]: # 頂点iに隣接する頂点を調べる
        if not visited[to] and cost[to] == cost[i] + c:
            # 未訪問かつ、iからtoへの辺が最短経路上の辺である場合
            # costには最短距離が入っているので、
            # toのcostがiのcost + cであれば、iからtoへの辺が最短経路上の辺である
            visited[to] = True
            path.append(to)
            dfs(to)
    path.pop() # 行き止まりに到達したら、そこまでの経路を削除して戻る
dfs(1) # 頂点1から開始(最小が1のため)

#########################################################
#########################################################

N, M = map(int, input().split())
# 重み付き無向グラフ
graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# ダイクストラ法(Dijkstra 法) + 経路復元
# ダイクストラ法の準備
import heapq
INF = 10**10 # 十分大きな値
cost = [INF] * (N + 1) # 始点(頂点1)から各頂点への 現時点での最短距離の暫定値（テンティティブ距離）を格納。 INFは未訪問
cost[1] = 0 # 頂点1までのコストは0
Q = [] # 優先度付きキュー
heapq.heappush(Q, (cost[1], 1)) # Qに(距離, 頂点)を格納

# 復元用の配列
back = [-1] * (N + 1) # 各頂点に対して、その頂点に最短距離で到達する直前の頂点を格納。-1は未訪問
# ダイクストラ法
while Q:
    c, pos = heapq.heappop(Q) # キューから最小要素を取り出す
    if cost[pos] != c: # 同じ頂点からを複数回探索しない
        continue
    else:
        for next in graph[pos]: # posに隣接する頂点を調べる
            next_pos, next_c = next
            if cost[next_pos] > cost[pos] + next_c:
                # next_posでcost[next_pos]よりも小さいコストで到達できる場合
                cost[next_pos] = cost[pos] + next_c
                back[next_pos] = pos # next_posに最短距離で到達する直前の頂点を格納
                heapq.heappush(Q, (cost[next_pos], next_pos)) # 現在のコストを優先度付きキューに追加

# 経路復元
ans = []
i = N
while i > 0:
    ans.insert(0, i)
    i = back[i]

# 結果の出力
# 経路は逆順に格納されているので、逆順に出力
print(*ans)
