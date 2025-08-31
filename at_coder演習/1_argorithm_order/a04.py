# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d
# A04 - Binary Representation 1
n = int(input())
binary_str = format(n, '010b')  # '0000000101'
# binary_str = bin(n)[2:].zfill(10)  # '0000000101'
print(binary_str)

