# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_am
# A62 - Depth First Search

N, M = map(int, input().split())

graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

success_text = "The graph is connected."
failed_text = "The graph is not connected."

# 深さ優先探索(DFS) = 再帰呼び出し
import sys
sys.setrecursionlimit(10**6) # 再帰上限を設定

def dfs(pos, G, visited):
    visited[pos] = True # 現在の頂点を訪問済みにする
    for to in G[pos]: # 隣接頂点を順に見る
        if not visited[to]:
            # 未訪問なら再帰的に訪問
            # その先を訪問し、その先の先を訪問し...と続き、
            # 最終的に行き止まりまで行ってから、そこから戻ってくる
            # （どこまでいけるかという深さを優先して探索する）
            dfs(to, G, visited)


visited = [False] * (N+1)
dfs(1, graph, visited) # 頂点1から開始(最小が1のため)

if all(visited[1:]): # すべて訪問済みか確認
    print(success_text)
else:
    print(failed_text)
    

