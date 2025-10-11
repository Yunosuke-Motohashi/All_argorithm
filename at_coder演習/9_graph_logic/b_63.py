# https://atcoder.jp/contests/tessoku-book/tasks/abc007_3
# B63 - 幅優先探索
H, W = map(int, input().split())
sx, sy = map(int, input().split())
sx -= 1 # indexに合わせる
sy -= 1
gx, gy = map(int, input().split())
gx -= 1
gy -= 1

grid = [input() for _ in range(H)]

# 幅優先探索(BFS)の準備
from collections import deque
distance = [[-1] * W for _ in range(H)] # 各マスまでの距離、-1は未訪問 -1とするのは距離が0のときの場合もあり得るため
distance[sx][sy] = 0 # スタート地点までの距離は0
Q = deque()
Q.append((sx, sy)) # スタート地点から探索開始

while Q: # キューが空になるまで繰り返す
    x, y = Q.popleft() # キューから先頭を取り出す
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # 4方向について調べる
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < H and 0 <= next_y < W: # マスが盤面の中にあるか
            if grid[next_x][next_y] == '.': # 移動先のマスが壁ではないか
                if distance[next_x][next_y] == -1: # 移動先のマスが未訪問か
                    distance[next_x][next_y] = distance[x][y] + 1 # 移動先のマスまでの距離を更新
                    Q.append((next_x, next_y)) # キューに追加する
                else:
                    # BFSでは最初に訪れたときが最短距離なので、
                    # 既に訪問済みなら何もしない
                    continue
# 結果の出力
print(distance[gx][gy])