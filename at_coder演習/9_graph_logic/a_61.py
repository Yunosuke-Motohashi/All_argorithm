# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bi
# A61 - Adjacent Vertices
N, M = map(int, input().split())

graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    if i == 0: continue
    output = ''
    output += str(i)
    output += ': {'
    output += ', '.join(map(str, g))
    output += '}'
    print(output)
