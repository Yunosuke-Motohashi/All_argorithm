# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k
# A11 - Binary Search 1
N, X = map(int, input().split())
A_l = list(map(int, input().split()))

l, r = 0, N-1
while l<=r:
    mid = (l+r)//2
    if A_l[mid] == X:print(mid+1); exit()
    elif A_l[mid] < X: l = mid +1
    else: r = mid -1
