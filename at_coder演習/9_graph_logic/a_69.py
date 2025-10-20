# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bq
# A69 - Bipartite Matching
# N人の生徒がいる
# 席の希望が入力値して与えられる
# 生徒iが席jに座ってもいい場合はCij=#、そうでない場合はCij=.
# 最大何人の希望を叶えられるか

"""
二部マッチング問題
二部マッチング問題とは、
頂点集合が左右二つに分かれたグラフで、
左右を結ぶ辺のうち互いに端点が共有しない辺を最大本数選ぶ問題。
つまり片側の各頂点が高々一つだけ相手と組になるよう最大の組数を求める。



この問題は、生徒の集合と席の集合の二つの部分集合に
分けられるグラフとしてモデル化できます。

最大フローのアルゴリズムを用いて解くことができます。
容量を１にして考えることで、各生徒が高々一つの席に座るようにできます。
"""


# 最大フローで解くためのグラフ構築
# 残余グラフを作成し、DFSで増加パスを探索する
class MaxflowEdge:
    """
    最大フロー用の辺の構造体
    """
    def __init__(self, to, cap, rev):
        self.to = to # 行き先
        self.cap = cap # 容量
        self.rev = rev # 逆辺のインデックス
    def __repr__(self):
        return f"Edge(to={self.to}, cap={self.cap}, rev={self.rev})"

# 深さ優先探索(DFS)
import sys
sys.setrecursionlimit(10**6) # 再帰上限を設定
def dfs(pos: int, goal:int, flow: int, graph, used: list):
    if pos == goal:
        # ゴールに到達したら、流量を返す
        return flow
    # 探索する
    used[pos] = True # これから探索する頂点を訪問済みに
    for next in graph[pos]:
        # 容量が1以上かつ、まだ訪問していない頂点のみにいく
        if next.cap > 0 and not used[next.to]:
            sent = dfs(next.to, goal, min(flow, next.cap), graph, used)
            # フローを流せる場合、
            # 残余グラフのその辺の容量を減らし、
            # 逆辺の容量を増やす
            if sent >= 1:
                next.cap -= sent
                graph[next.to][next.rev].cap += sent
                return sent
    return 0 # ゴールに到達できなかった場合は0を返す

def max_flow(N, s, t, edges):
    # 初期状態の残余グラフを構築
    graph = [list() for _ in range(2*N + 2)] # 頂点0~N-1: 生徒、N~2N-1: 席、2N: ソース、2N+1: シンク
    for a, b, c in edges:
        # 順方向の辺を追加, 逆辺のインデックスはこれから追加される逆方向の辺の位置は(len(graph[b]))となる
        graph[a].append(MaxflowEdge(b, c, len(graph[b])))
        # 逆方向の辺を追加, 逆辺のインデックスは先に追加され他ので、順方向の辺の位置は(len(graph[a]) - 1)となる
        graph[b].append(MaxflowEdge(a, 0, len(graph[a])-1))
    INF = 10**9
    total_flow = 0
    while True:
        used = [False] * (2*N + 2) # 各頂点の訪問済みフラグ
        flow = dfs(s, t, INF, graph, used)
        if flow == 0:
            # これ以上フローを流せない場合は終了
            break
        # フローを流せた場合、合計フローに加算
        total_flow += flow
    return total_flow


N = int(input())
C = [ input() for _ in range(N)]

# 最大フローを求めたいグラフを構築する
# 辺の要素は(辺の始点, 辺の終点, 辺の容量)のタプル
# 生徒の頂点: 1~N
# 席の頂点: N+1~2N
# ソースの頂点: 0
# シンクの頂点: 2N+1
edges = []
for i in range(N):
    for j in range(N):
        if C[i][j] == '#':
            # i番の生徒はj番の席に座ってもよい
            # 生徒i+1, 席 N+j+1
            # 容量1の辺を追加
            edges.append((i+1, N+j+1, 1))

source = 0
sink = 2*N + 1
for i in range(N):
    # ソース(0)から各生徒への容量1の辺を追加
    edges.append((source, i+1, 1))
    # 各席からシンク(2N+1)への容量1の辺を追加
    edges.append((N+i+1, sink, 1))

# 最大フローを求める
ans = max_flow(N, source, sink, edges)
print(ans)