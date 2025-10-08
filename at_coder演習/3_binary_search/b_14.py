# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm
# B14 - Another Subset Sum
N, K = map(int, input().split())
A_l = list(map(int, input().split()))

## Kになる組み合わせが有るか無いか
## 全検索だと最大 2 ** 30 で約10 ** 9 で間に合わない

# 配列を半分に分けて、それぞれで取りうる和を全探索
# 最大 2 ** 15 を2回で約 2 * 10 ** 4 で間に合う
def make_sum_list(A) -> list:
    sum_list = []
    for bit in range(1 << len(A)):
        # 0から2**len(A)-1までのbit全探索
        sum = 0
        for i in range((len(A))):
            if bit & (1 << i):
                # i番目が1かかくにんする, i盤面が0の時は&演算で0になる
                sum += A[i]
        sum_list.append(sum)
    return sum_list

lefts = A_l[:N//2]
rights = A_l[N//2:]
left_sums = make_sum_list(lefts)
right_sums = make_sum_list(rights)

# 片方の和を固定して、もう片方でK-和があるかを二分探索で探索
import bisect
right_sums.sort()
for ls in left_sums:
    target = K - ls
    pos = bisect.bisect_left(right_sums, target)
    if pos<len(right_sums) and K == right_sums[pos] + ls:
        # 検算して、Kと等しいか確認
        print("Yes")
        exit()
print("No")
