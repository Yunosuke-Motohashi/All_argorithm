# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e
# A05 - Three Cards
n, k = map(int, input().split())

# nums = set()
cnt = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        z = k - x - y
        if z > 0 and z <= n:
            # nums.add((x, y, z))
            cnt += 1
print(cnt)
