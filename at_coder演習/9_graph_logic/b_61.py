# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eh
# B61 - Influencer

N, M = map(int, input().split())

graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
max_v = 0
for i in range(1, N+1):
    if max_v < len(graph[i]):
        max_v = len(graph[i])
        ans = i
print(ans)