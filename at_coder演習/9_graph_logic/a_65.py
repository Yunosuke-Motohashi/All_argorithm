# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bm
# A65 - Road to Promotion
N = int(input())
A_l = list(map(int, input().split())) # 社員２〜Nの上司
A_l = [0] * 2 + A_l # indexを社員番号に合わせるために先頭に0, 0を追加

# DPで
graph = [ list() for _ in range(N+1)] # graph[i]: 社員iの部下のリスト
for i in range(2, N+1): # 2〜Nの社員について上司を確認
    boss = A_l[i]
    graph[boss].append(i) # 上司 -> 部下としてグラフを作成
# print(graph)
ans = [0] * (N+1) # ans[i]: 社員iの部下の人数
for i in range(N, 0, -1): # 社員Nから社員1(社長)に向かって調べる
    for j in graph[i]: # 社員iの部下jについて
        ans[i] += ans[j] + 1 # 部下jの部下の人数 + 1(部下j自身)を加える

print(*ans[1:])
