# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bp
# A68 - Maximum Flow
# aからbへ毎秒cリットルの水を流せる
# 1からNまで毎秒最大何リットルの水を流せるか
# 1からNまでの間に何リットルあるか、つまり、最大フローを求める問題

"""
最大フロー問題
グラフ理論における最大フロー問題とは、各辺に容量制限のあるグラフにおいて、
単一の始点（ソース）から単一の終点（シンク）の間に流れるものの最大量を求める問題です。

フォード・ファルカーソン(Ford-Fulkerson)法で解ける
フローネットワークにおいて、残余容量が存在する限り、
増加パスを探索しフローを増加させ続けることで、
最終的に最大フローに到達します。

"""


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
    """
    posからgoalまでどれくらいの流量を流せるか探索する
    - goalまで到達できるpathがあれば、そのpathの最小容量を返す
    - 到達できない場合は0を返す
    途中で訪問済みの頂点には行かないようにする
    """
    if pos == goal:
        # ゴールに到達したら、流量を返す
        return flow
    # 探索する
    used[pos] = True # これから探索する頂点を訪問済みにする
    for next in graph[pos]:
        # 容量が1以上かつ、まだ訪問していない頂点のみにいく
        if next.cap > 0 and not used[next.to]:
            # next.toへflowとnext.capの小さい方を流せるか探索
            # flowと分けるために、sentに代入
            # sent: next.toへ実際に流せる量
            sent = dfs(next.to, goal, min(flow, next.cap), graph, used)
            # フローを流せる場合、
            # 残余グラフのその辺の容量を減らし、
            # 逆辺の容量を増やす
            if sent >= 1:
                next.cap -= sent
                graph[next.to][next.rev].cap += sent
                return sent
    # ゴールに到達できなかった場合は0を返す
    return 0


def max_flow(N:int, edges: list, source: int, sink: int):
    """残余グラフを用いたフォード・ファルカーソン法で最大フローを求める
    N: 頂点数
    graph: 辺のリスト (a, b, c) aからbへ
    source: 始点
    sink: 終点
    返り値: 最大フロー
    """
    # 初期状態の残余グラフを作成
    graph = [list() for _ in range(N+1)]
    for a, b, c in edges:
        # 順方向の辺を追加, 逆辺のインデックスはこれから追加される逆方向の辺の位置は(len(graph[b]))となる
        graph[a].append(MaxflowEdge(b, c, len(graph[b])))
        # 逆方向の辺を追加, 逆辺のインデックスは先に追加され他ので、順方向の辺の位置は(len(graph[a]) - 1)となる
        graph[b].append(MaxflowEdge(a, 0, len(graph[a])-1))
    INF = 10**9
    total_flow = 0
    while True:
        # 毎回探索前に訪問済みリストを初期化
        used = [False] * (N+1)
        flow = dfs(1, N, INF, graph, used) # 1からNまでの増加パスを探索
        if flow > 0:
            total_flow += flow
        else:
            # これ以上フローを流せなくなったら終了
            break
    return total_flow

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
ans = max_flow(N, edges, 1, N)
print(ans)

