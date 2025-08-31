# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
# B02 - Divisor Check
n = 100
n_divisors = [i for i in range(1, n+1) if n % i == 0]
a, b = map(int, input().split())
for i in range(a, b+1):
    if i in n_divisors:
        print("Yes")
        exit()
    else:
        continue
print("No")