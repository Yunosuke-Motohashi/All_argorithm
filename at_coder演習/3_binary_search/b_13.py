# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cl
# B13 - Supermarket 2

# Nのmaxは10**5 組み合わせは（N+1）*N/2  = 5*10**9 のでTLEになりそう


N, K = map(int, input().split())
A_l = list(map(int, input().split()))

# 累積和
S = [0] * (N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + A_l[i-1]

def check(l, r):
    return S[r+1] - S[l] <= K

# 右端のインデックスを保存する配列
R = [None] * N

ans = 0
for i in range(N):
    if i == 0:
        # i=0のときは左端が0なので右端は-1からスタート
        R[i] = -1
    else:
        # i>0のときは左端がiなので右端はR[i-1]からスタート
        R[i] = R[i-1]
    # 右端を1つ進めて確認し、条件を満たす限り進める
    while R[i] < N-1 and check(i, R[i]+1):
        R[i] += 1
for i in range(N):
    # 左端がiなので、右端がR[i]で
    # 答えとなるのは iからR[i]までの個数となり、
    # 端の数を含むので+1する
    ans += R[i] - i + 1
print(ans)
