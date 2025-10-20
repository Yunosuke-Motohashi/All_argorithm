# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_br
# A70 - Lanterns
# N個のランタンがある
# M種類の操作ができる、各操作はX, Y, Zのランタンを同時に反転できる
# 最小何回の操作で全てONにできるか

"""
初期状態のランタンのON/OFF情報をビットで表現し、
目的の状態もビットで表現（全てON=111...1）
各操作で反転するビットを指定して、
各操作をビット演算のXORで表現して、
幅優先探索で最短手数を探索する
"""
N, M = map(int, input().split())
A_l = list(map(int, input().split()))

# 操作のリスト　0-indexに対応するため-1しておく
operations = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

# 反転 → XOR演算で実装

# 初期状態をビットで表した10進数に変換
start = 0
for i in range(N):
    # A_l[i]が0 or 1なので、2のi乗を掛けるだけでOK
    start += A_l[i] * (2 ** i)
# start: 初期のビット状態を10進数で表現したもの
# goal: 全てONの状態なので,
# そのビット状態(1<<N)-1を10進数で表したもの 2^N-1
goal = 2 ** N - 1

# 幅優先探索(BFS)で最短手数を探索
from collections import deque
dist = [-1] * (2 ** N) # goalまでの最短手数、-1は未訪問
Q = deque() # キュー
dist[start] = 0 # 初期状態までの手数は0
Q.append(start) # 初期状態をキューに追加

while Q: # キューが空になるまで繰り返す
    pos = Q.popleft() # キューから先頭を取り出す
    for x, y, z in operations:
        # 次の状態を計算
        # 反転操作はXOR演算で実装（1^1 → 0, 1^0 → 1）
        # x, y, z番目のビットを指定して反転するため、
        # x番目のビットを1にした数(1<<x)と
        # y番目のビットを1にした数(1<<y)と
        # z番目のビットを1にした数(1<<z)を
        # XOR演算でまとめて反転する
        next = pos ^ (1 << x) ^ (1 << y) ^ (1 << z)
        # next = pos ^ ((1 << x) | (1 << y) | (1 << z)) # これと同じ
        if dist[next] == -1: # nextが未訪問の場合
            dist[next] = dist[pos] + 1 # nextまでの操作回数を更新
            Q.append(next) # キューに追加する
# 結果の出力
print(dist[goal])
