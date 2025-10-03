# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al
# B07 - Convenience Store 2
T = int(input())
N = int(input())
part_times = [0] * (T+1)
for _ in range(N):
    L, R = map(int, input().split())
    part_times[L] += 1
    part_times[R] -= 1
for i in range(1, T):
    part_times[i] += part_times[i-1]
print(*part_times[:T], sep="\n", end="")
