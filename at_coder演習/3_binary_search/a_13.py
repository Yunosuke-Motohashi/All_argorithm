# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m
# A13 - Close Pairs
N, K = map(int, input().split())
A_l = list(map(int, input().split()))
j= 0
ans = 0
for i in range(N):
    a = A_l[i]
    # jを可能な限り進める　昇順のため jは初期化する必要はない
    while j < N and A_l[j] - a <= K:
        j += 1
    ans += j-i-1
print(ans)
