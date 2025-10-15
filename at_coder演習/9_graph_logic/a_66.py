# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bn
# A66 - Connect Query
# N, Q = map(int, input().split())

# graph = [list() for _ in range(N+1)]
# for _ in range(Q):
#     flg, u, v = map(int, input().split())
#     if flg == 1:
#         graph[u].append(v)
#         graph[v].append(u)
#     else: # flg == 2
#         if v in graph[u]:
#             print("Yes")
#         else:
#             print("No")


# グループが同じかどうかを判断するので、頂点からの連結要素だけではわからない
# そこで、Union-Find木を使う

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

N, Q = map(int, input().split())
uf = UnionFind(N) # Union-Find木の初期化
for _ in range(Q):
    flg, u, v = map(int, input().split())
    if flg == 1:
        # 頂点uと頂点vを結合
        uf.unite(u, v)
    else: # flg == 2
        # 頂点uと頂点vが同じグループに属するかどうかを判定
        if uf.same(u, v):
            # 同じグループに属する場合
            print("Yes")
        else:
            # 異なるグループに属する場合
            print("No")