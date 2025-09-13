# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai
# A06 - How Many Guests?
n, q = map(int, input().split())
a_l = list(map(int, input().split()))
sums = [a_l[0]] * n
for i in range(1,n):
    sums[i] = sums[i-1] + a_l[i]

for _ in range(q):
    l, r = map(int, input().split())
    if l == 1:
        print(sums[r-1])
    else:
        print(sums[r-1] - sums[l-2])
