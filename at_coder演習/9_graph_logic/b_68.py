# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eo
# B68 - ALGO Express
# N個の駅がある
# 特急を０個以上の駅を指定して停車駅とする
# i駅を特急駅にすると、Pi円の利益が見込める（Piは負の場合もある）
# 「駅Ajを特急駅にするなら、駅Bjも特急駅にするべき」というM個の提案がある
# これらの提案をすべて満たしつつ、利益の最大化を図る


"""
このファイルで使う考え方のメモ。

■ 最大クローズド集合
ある頂点を選んだら、その頂点から進める辺の行き先も必ず選ばないといけないような頂点集合。
今回の「駅 A を選ぶなら駅 B も選ぶべき」という制約がちょうどこの形になっている。

■ カットとその容量
頂点集合をソース側 S とシンク側 T に分けたとき、S から T へ向かう辺たちの容量を全部足し合わせた値がカット容量。
“どの辺を切ればソースからシンクへ流れなくなるか”を数値化したもの、と考えるとわかりやすい。

■ 最大フロー最小カット定理
ソースからシンクへ流せる最大流量と、最小カットの容量は必ず同じ値になる。
この性質を使って「最大利益 = 正の利益合計 − 最小カット容量」を導き出す。
"""
INF = 10**9

# 残余グラフを作成し、DFSで増加パスを探索する
class MaxflowEdge:
    """Ford-Fulkerson 法で扱う 1 本の辺。

    Attributes
    ----------
    to : int
        辺の行き先の頂点番号。
    cap : int
        残余容量。今この辺にまだどれだけフローを流せるかを表す。
    rev : MaxflowEdge
        「逆辺」への参照。フローを戻すときに容量を増やすために使う。
    """

    def __init__(self, to, cap, rev):
        self.to = to   # 行き先
        self.cap = cap # 現時点の残余容量
        self.rev = rev # 対応する逆辺（後から代入する）

class FordFulkerson:
    def __init__(self, N):
        self.size = N  # 頂点数（ソース・シンクを含めた総数）
        self.graph = [list() for _ in range(N)]  # 残余グラフを隣接リストで保持

    def add_edge(self, fr, to, cap):
        """
        有向辺 fr→to（容量 cap）と、その逆辺 to→fr（容量 0）を残余グラフに追加する。

        Ford-Fulkerson 法では「ある辺にフローを流したあと、必要になったら戻す」処理が発生する。
        そのため、順方向と逆方向の辺をペアで登録し、逆方向の辺の容量をフロー分だけ増やすことで
        “あとから引き返す”動きを表現している。
        """
        forward = MaxflowEdge(to, cap, None)      # 順方向の辺。最初は cap だけ流せる。
        backward = MaxflowEdge(fr, 0, forward)    # 逆方向の辺。まだ何も流していないので容量 0。
        forward.rev = backward                    # 相互参照を張っておくと更新が楽になる。
        self.graph[fr].append(forward)            # 順方向の辺を登録
        self.graph[to].append(backward)           # 逆方向の辺を登録
    
    def dfs(self, i, goal, F):
        # 現在位置がゴールなら、ここまでの経路で流せる量（ボトルネック）を返す
        if i == goal:
            return F
        
        self.visited[i] = True  # 同じ頂点をぐるぐる回らないようマークしておく

        for e in self.graph[i]:  # 頂点 i から出るすべての辺を順に試す
            if e.cap == 0:
                # もう余裕が無い辺はこの経路に使えないのでスキップ
                continue
            if self.visited[e.to]:
                # 既に訪れた頂点に戻ると無限ループになるためスキップ
                continue
            # この辺を選んだ場合のボトルネックは「これまでの最小値」と「この辺の容量」の小さい方。
            flow = self.dfs(e.to, goal, min(F, e.cap))
            if flow > 0:
                # ゴールまでの増加路が見つかったので、残余グラフを更新する。
                e.cap -= flow          # 順方向の容量から流した分だけ減らす
                e.rev.cap += flow      # 逆方向の容量を同じ分だけ増やす（戻りの余地ができる）
                return flow
        # どの辺を辿ってもゴールへ届かなかったので、この経路では流せる量は 0。
        return 0

    def max_flow(self, s, t):
        """
        ソース s からシンク t まで、合計でどれだけフローを流せるか（最大フロー）を求める。
        """
        ans = 0
        while True:
            self.visited = [False] * self.size
            # ボトルネックの初期値を INF にして DFS を開始する。
            # DFS の中で経路ごとの最小容量に順次更新され、結果的に「その経路で流せる最大量」になる。
            F = self.dfs(s, t, INF)
            if F == 0: # これ以上流せない場合は終了
                break
            ans += F # 見つかったフロー量を積み上げる
        return ans

N, M = map(int, input().split())
P = list(map(int, input().split()))
proposals = [ list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]


# グラフの構築
S = N # ソースの頂点番号
T = N+1 # シンクの頂点番号
ff = FordFulkerson(N + 2) # 頂点数N + ソース + シンク

offset = 0 # 正の利益の合計。後で最小カット値を引くための補正項。
for i in range(N):
    if P[i] >= 0:
        # 駅 i を特急駅にすると +P[i] の利益が得られるケース。
        # 「特急駅にしない」判定は、ソース→駅 i の辺をカットすることに対応させる。
        # そのためソースから駅 i へ容量 P[i] の辺を張り、カットされたときに利益 P[i] を失うようにしている。
        ff.add_edge(S, i, P[i])
        offset += P[i]  # 正の利益をあらかじめ合計しておき、最後に失われた分を差し引く
    else:
        # 駅 i を特急駅にすると損失が出る（P[i] が負）ケース。
        # 駅 i →シンク T の辺に容量 -P[i] を設定し、駅 i を選んだ場合にその損失を支払う形に変換する。
        ff.add_edge(i, T, -P[i]) 

for a, b in proposals:
    # 制約「駅 a を特急駅にするなら駅 b も特急駅にする」を残余グラフで表現する。
    # A→B に十分大きい容量（実質無限大）を置いておけば、A をソース側に残したとき
    # 必ず B もソース側に残らざるを得なくなる。
    ff.add_edge(a, b, INF)

max_profit = offset - ff.max_flow(S, T)
print(max_profit)


"""
（メモ）
上の入力例では、ソース S は駅 0・1・4 へそれぞれ容量 3, 4, 5 の辺を持ち、
駅 2・3 はシンク T へそれぞれ 1, 5 の辺を持つ。さらに制約のために
0→2, 1→3 へ大きな容量の辺が追加される。
この構造のおかげで、カットが駅を「選ぶ／選ばない」の判定と一対一対応する。
"""