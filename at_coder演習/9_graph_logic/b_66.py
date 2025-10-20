# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_em
# B66 - Typhoon
# N個の駅とM本の路線がある
# i本目の路線は駅a_iと駅b_iを双方向に結んでいる
# クエリ1 - x本目の路線を使えなくする
# クエリ2 - 駅sから駅tへ行けるかどうかを答える

# Union-Find木で解く
class UnionFind:
    def __init__(self, n):
        self.n = n
        # parent[i]: 頂点iの親ノード、-1は根ノードであることを示す 
        self.parent = [-1] * (n+1)
        # size[i]: 頂点iの属するグループの、要素数
        self.size = [1] * (n+1)

    def root(self, x):
        """
        頂点xの根ノードを返す
        """
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

    def same(self, u, v):
        """
        要素 u, v が同じグループに属するかどうかを判定する関数
        """
        return self.root(u) == self.root(v)
    
    def unite(self,u,v):
        """
        要素 u, v を統合する関数
        大きいグループに小さいグループを結合する
        """
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]

"""
Union-Findは、辺削除に対応できないため、オフライン逆順処理で解く。
辺を削除する代わりに、すべてのクエリを記録してから逆順に処理する。
最後まで残る路線だけで初期的に DSU を構築し、逆順で「削除クエリ」を辺追加として扱い、
「到達判定クエリ」で連結性を確認して結果を記録する。

手順：
1. 入力全体を読み、クエリ1で指定される路線番号をすべて記録する。
2. 「最後まで残る路線」だけで Union-Find を初期化し、削除されない路線を順に unite する。
3. クエリ列を末尾から逆順に処理する。クエリ1は「路線復活」とみなし、対応する辺を unite。
4. クエリ2は逆順でも到達判定なので、その場で same を評価し結果を配列に保持。
5. 逆順処理が終わったら結果配列を逆に出力して完了。
"""
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]
# クエリ1で削除される路線を記録
last_edges = [True] * M # 最後まで残る路線のフラグ
for query in queries:
    if query[0] == 1:
        # x本目の路線は最後まで残らない
        x = query[1]
        last_edges[x-1] = False


uf = UnionFind(N) # Union-Find木の初期化
# 最後まで残る路線だけでUnion-Find木を構築
for i in range(M):
    if last_edges[i]:
        a, b = edges[i]
        uf.unite(a,b)

# クエリを逆順に処理
ans = []
for query in reversed(queries):
    if query[0] == 1:
        # クエリ1: 路線を復活させる
        x = query[1]
        a, b = edges[x-1]
        uf.unite(a,b)
    else:
        # クエリ2: 駅sから駅tへ行けるか判定
        s, t = query[1], query[2]
        if uf.same(s, t):
            ans.append("Yes")
        else:
            ans.append("No")


# 結果を逆順に出力
for res in reversed(ans):
    print(res)

