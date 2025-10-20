# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_el
# B65 - Road to Promotion Hard
# a bが与えられ、aとbは直属の上司or部下の関係にある
# 部下がいない社員のrankは0
# それ以外の社員のrankは、直属の部下のrankの最大値+1
# 社員Tが社長

# ツリー状のグラフを作る必要がある

N, T = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
rank = [0] * (N+1) # rank[i]: 社員iのランク


# Tから辿れば上下関係がわかる
# 深さ優先探索で部下側からランクを計算
import sys
sys.setrecursionlimit(1 << 30)  # 再帰上限をなくす
def dfs(parent: int, i: int):
    """社員 i を根とする部分木から、ランクを再帰的に計算する。
    Args:
        parent (int): 直前に訪れた社員（親ノード）の番号。戻りを防ぐために利用。
        i (int)     : 現在ランクを求めたい社員（ノード）の番号。
    Returns:
        int: 社員 i のランク（直属の部下の最大ランク + 1、部下がいなければ 0）。
    """
    # 社員iのrankを計算する
    # 部下がいない場合は、親以外の隣接社員がいないのでrankは0でそのまま返す
    for to in graph[i]: # 社員iの隣接社員toについて
        if to == parent:
            continue # parentのノードはすでに見ているので、戻らない(スルーする)
        r = dfs(i, to) + 1 # 部下社員toについて再帰的に調べ、部下のランクに 1 を足した値が候補
        if r > rank[i]:
            # 今のまでのrank[i]より大きければ更新
            rank[i] = r
    return rank[i] # 社員iのrankを返す

dfs(-1, T) # 社長Tから開始
print(*rank[1:])

