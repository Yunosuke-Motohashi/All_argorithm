N = int(input())
A_l = list(map(int, input().split()))

# (index, value) の降順リスト
index_value_pairs = sorted(((i,a) for i, a in enumerate(A_l)), key=lambda x: x[1], reverse=True)


D = int(input())
for _ in range(D):
    L, R = map(int, input().split())
    for index, value in index_value_pairs:
        if not (L <= index+1 <= R):
            print(value)
            break

