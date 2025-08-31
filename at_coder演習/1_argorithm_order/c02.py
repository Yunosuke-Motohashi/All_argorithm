# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ez
# C02 - Two Balls
n = int(input())
a_l = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans = max(ans, a_l[i] + a_l[j])

print(ans)
