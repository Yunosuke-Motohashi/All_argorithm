# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b
# A02 - Linear Search
n, x = map(int, input().split())
a_l = list(map(int, input().split()))

if x in a_l:
    print("Yes")
else:
    print("No")
