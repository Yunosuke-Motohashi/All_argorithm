# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
# A12 - Printer
N, K = map(int, input().split())
A_l = list(map(int, input().split()))

l, r = 1, 10 ** 9
while l < r:
    mid = (l+r)//2
    sum = 0
    # mid時点での合計枚数
    for a in A_l:
        sum += mid // a
    if sum >= K:
        r = mid
    else:
        l = mid + 1
print(l)