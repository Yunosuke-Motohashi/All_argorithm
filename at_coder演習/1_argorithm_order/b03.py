# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
# B03 - Supermarket 1
"""異なる 3 つの商品を選び、
合計価格をピッタリ 1000 円にする方法は存在しますか
"""
n = int(input())
a_l = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a_l[i] + a_l[j] + a_l[k] == 1000:
                print("Yes")
                exit()
print("No")
