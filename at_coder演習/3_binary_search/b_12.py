# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck
# B12 - Equation
def f(x):
    return x ** 3 + x

N = int(input())

l, r = 0.0, 100.0

mid = (l + r) / 2

v = f(mid)
## 流石に100回もやれば十分
for _ in range(100):
    mid = (l + r) / 2
    v = f(mid)
    if v > N:
        r = mid
    else:
        l = mid
print(mid)
