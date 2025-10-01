# B06 - Lottery
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce

N = int(input())
A_l = list(map(int, input().split()))

sums = [A_l[0]] * N
for i in range(1,N):
    sums[i] = sums[i-1] + A_l[i]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    hit_rate = (sums[R-1] - sums[L-1] + A_l[L-1]) / (R-L+1)
    if hit_rate > 0.5:
        print("win")
    elif hit_rate == 0.5:
        print("draw")
    else:
        print("lose")
