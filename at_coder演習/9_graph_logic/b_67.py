# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_en
# B67 - Max MST
# N, M : 頂点数、辺数
# A, B, C: 各辺の情報（頂点A, 頂点B, 重みC） 双方向の辺
# このグラフの最大全域木の総和を求める

"""
最大全域木とは
グラフのすべての頂点を含み、
かつ閉路を持たない部分グラフのうち、辺の重みの和が最大となるもの
"""

"""
クラスカル法で重い順に辺を追加していく
1. 辺を重みの降順にソート
2. Union-Findでサイクルを検出しながら、辺を追加
    サイクルができる場合は追加しない
3. 追加した辺の重みの和が最大全域木の重み
"""

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
# 辺を重みの降順にソート
edges.sort(key=lambda x: x[2], reverse=True)

# Union-Find木の初期化
uf = UnionFind(N)
# 最大全域木(MaxSpanningTree)のコスト計算
max_mst_cost = 0
# 最大全域木の構築
for a, b, c in edges:
    # 辺(a, b)を追加してもサイクルができない場合、辺を追加
    if not uf.same(a, b):
        uf.unite(a, b)
        max_mst_cost += c

print(max_mst_cost)