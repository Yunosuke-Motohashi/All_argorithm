# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bo
# A67 - MST (Minimum Spanning Tree)

# 最小全域木とは、
# 重み付き無向グラフにおいて、全ての頂点を含み、
# かつ、全ての頂点が連結している部分グラフのうち、辺の重みの和が最小となるもの

# union find木による最小全域木のコスト計算

# Union-Find 木の実装
class UnionFind:
    """ 頂点nのUnnion-Find木を作成
     n: 頂点数
     頂点は1〜nまでの番号を持つとする
     親ノードを管理するparent配列と、グループの要素数を管理するsize配列を持つ
     parent[i]: 頂点iの親ノード、-1は根ノードであることを示す
     size[i]: 頂点iの属するグループの、要素数
    """
    def __init__(self, n):
        self.n = n # 頂点
        # parent[i]: 頂点iの親ノード、-1は根ノードであることを示す 
        self.parent = [-1] * (n+1) # 最初は全て根ノード（親ノードがない）
        # size[i]: 頂点iの属するグループの、要素数
        self.size = [1] * (n+1) # 最初は全て1
    
    def root(self, x):
        """
        頂点xの根ノードを返す
        """
        while self.parent[x] != -1:
            # 根ノードになるまで親ノードをたどる
            x = self.parent[x]
        return x

    def unite(self, u, v):
        """
        要素 u, v を統合する関数
        """
        # u, vの根ノードを取得する
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            # 根ノードが異なる、つまり、u, vが異なるグループに属している場合
            # uとvが属するグループを結合する
            if self.size[root_u] < self.size[root_v]:
                # vが属するグループの方が大きい場合
                # vの根ノードをuの根ノードにする。つまり、uのグループをvのグループに結合する
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u] # vのグループの要素数を更新
            else:
                # uが属するグループの方が大きい場合(同じも含む)　>=
                # uの根ノードをvの根ノードにする。つまり、vのグループをuのグループに結合する
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v] # uのグループの要素数を更新

    def same(self, u, v):
        """
        要素 u, v が同じグループに属するかどうかを判定する関数
        """
        # u, vの根ノードを確認し、根ノードが同じなら、uとvは同じグループに属する
        return self.root(u) == self.root(v)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Kruskal（クラスカル）法で最小全域木（MST）の総コストを求める。
"""
Kruskal（クラスカル）法
 - 辺集合 E をコストの小さい順にソートする
 - 以下を V-1 個の辺を選ぶまで（最小全域木 T ができるまで）繰り返す
   - 残っている辺の中からコストが最小の辺 e を取り出す。
     現在構成中の T に e を加えても閉路ができないなら T に加える。
"""
# コストが小さい順にedges(辺集合)をソート
edges.sort(key = lambda x: x[2])
ans = 0
uf = UnionFind(N) # Union-Find木の初期化
# 最小全域木を作っていく
for a, b, c in edges:
    if not uf.same(a, b):
        # aとbが異なるグループに属している場合
        # つまり、aとbを結んでも閉路ができない場合
        # （閉路ができると、ループができてしまい、最小全域木ではなくなる）
        uf.unite(a, b) # aとbのグループを結合
        ans += c # 最小全域木コストを加算していく

print(ans)