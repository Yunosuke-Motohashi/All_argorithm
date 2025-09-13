# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
# A07 - Event Attendance
d = int(input())
n = int(input())

attendance = [0] * (d+1)

for _ in range(n):
    l, r = map(int, input().split())
    attendance[l-1] += 1
    attendance[r] -= 1

for i in range(1,d):
    attendance[i] += attendance[i-1]

print(*attendance[:d], sep="\n", end="")
