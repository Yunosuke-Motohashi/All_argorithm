# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ei
# B62 - Print a Path

N, M = map(int, input().split())

graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 深さ優先探索(DFS)の準備
import sys
sys.setrecursionlimit(10**6) # 再帰上限を設定
path = []
visited = [False] * (N+1)
def dfs(i: int):
    path.append(i)
    if i == N: # ゴールに到達したら
        # 答えを出力して終了
        # print(*path)
        for x in path:
            print(x) # この形式でないと正解にならない
        sys.exit() # 終了
    else:
        visited[i] = True
        for to in graph[i]:
            if not visited[to]:
                # 未訪問なら再帰的に訪問
                dfs(to)
        path.pop() # 行き止まりに到達したら、そこまでの経路を削除して戻る

dfs(1) # 頂点1から開始(最小が1のため)