# http://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
# A56 - String Hash
# 各クエリでa, b, c,　dが与えれらる
# S[a,b] と S[c,d] が等しいかどうかを判定する問題
# S[l,r]はSのl番目からr番目までの連続部分文字列


"""
=== ローリングハッシュ (Rolling Hash) ===
Rolling Hash とは、列のハッシュを高速に計算できるハッシュアルゴリズムです。
累積ハッシュを事前計算することで、任意の部分文字列のハッシュ値をO(1)で取得可能。
# ハッシュ関数の定義
数列 A = [a_1, a_2, ..., a_n] のハッシュ値 H(A) を以下のように定義します。
ローリングハッシュ関数R
R(A) = (a_1 * x^(n-1) + a_2 * x^(n-2) + ... + a_n * x^0) mod p
- x: 基数（base）。通常は素数を選ぶ（例：31, 37, 1009など）
- p: 大きな素数（MOD）。例：2147483647 など
- n: 数列の長さ
# 左からの累積ハッシュ計算
H[i] = (H[i-1] * base + S[i-1]) mod p

基数とは桁を表す数のことで、例えば10進数では基数は10です。
ローリングハッシュでは、基数を適切に選ぶことで、文字列の各文字を数値に変換し、その数値を基数の累乗で重み付けしてハッシュ値を計算します。

mod p は、計算結果が非常に大きくなるのを防ぐために使用される操作で、pは大きな素数です。これにより、ハッシュ値が一定の範囲内に収まります。

基数の選び方
< 256 >
-> ASCII文字の範囲が0-255（256種類）をカバー
   すべてのASCII文字を自然に区別できる
   文字コード(ord())がそのまま使えるので実装が簡単
   ただし、baseとmodが互いに素でない場合に衝突しやすい
   UTF-8など広い範囲の文字を扱う場合は不向き

< 素数 (31, 37, 1009など)>
-> 衝突を減らす効果がある
   文字列のパターンが偏っている場合に有効
   ハッシュ値の分布が均一になりやすい

< 大きい素数 (例えば10007, 100003など)>
-> ハッシュ値の範囲を広げ、衝突をさらに減らす
   UTF-8など広い範囲の文字を扱う場合
-> 中程度の素数（4桁〜6桁程度）
   256より大きいため、ASCII以外の文字も扱いやすい
   素数なのでmodと互いに素になりやすい
   大きすぎないので計算も重くない

modに大きな素数を使う理由(例えば10^9+7や2^61-1)
-> 衝突を減らす つまり 0~その素数-1までのハッシュ値に均等に分布させる
-> ハッシュ値の分布を均一にする
-> 計算の安定性を保つ


シングルハッシュとダブルハッシュ
シングルハッシュ: 一つのハッシュ関数を使用
-> 実装が簡単
-> 衝突の可能性が高い
ダブルハッシュ: 二つの異なるハッシュ関数を使用
-> 異なる基数とMODの組み合わせを2セット用意
-> 両方のハッシュが一致して初めて「同じ」と判定
-> 衝突確率が（シングルの確率）^2 になる
   例: シングルで 10^-6 なら、ダブルで 10^-12
-> 競技プログラミングで強く推奨される


先に冪乗を計算しておくことで、部分文字列のハッシュ値の計算がO(1)で可能になる
毎回 base ** (length of substring) を計算する必要がなくなるため高速化できる
"""

class RollingHashPalindrome:
    """ローリングハッシュを用いた文字列の部分一致・回文判定クラス"""
    def __init__(self, S, base, mod):
        self.N = len(S)
        self.base = base
        self.mod = mod
        self.pow_base = [1] * (self.N + 1)
            
        self.H_forward = self._compute_forward_hash(S)
        self.H_backward = self._compute_backward_hash(S)

    def _compute_forward_hash(self, S):
        H = [0] * (self.N + 1)
        for i in range(1, self.N + 1):
            H[i] = (H[i-1] * self.base + ord(S[i-1])) % self.mod
            self.pow_base[i] = self.pow_base[i-1] * self.base % self.mod
            # pow_base[i]: baseのi乗 の modした値。modしておかかないと大きくなりすぎる
            # このタイミングで計算しておくことで、一回のループで済む
            # 後で部分文字列のハッシュ値を計算する際に使える
        return H

    def _compute_backward_hash(self, S):
        H = [0] * (self.N + 1)
        for i in range(self.N-1, -1, -1):
            # i: N-1, N-2, ..., 0
            # idx: 1, 2, ..., N
            idx = self.N - i # self.N - 1 - i + 1
            H[idx] = (H[idx-1] * self.base + ord(S[i])) % self.mod
        return H
    
    def get_hash_forward(self, l, r):
        """S[l:r]のハッシュ値を取得する（0-based、左から右）"""
        hash = (self.H_forward[r] - self.H_forward[l] * self.pow_base[r-l] ) % self.mod
        return hash
    
    def get_hash_backward(self, l, r):
        """S[l:r]を逆順にした文字列のハッシュ値を取得する（0-based）
        後ろから計算した累積ハッシュから、S[l:r]に対応する部分を抽出する。
        これにより S[r-1:l-1:-1]（S[l:r]の逆順）のハッシュ値が得られる。"""
        hash = (self.H_backward[self.N-l]- self.H_backward[self.N-r] * self.pow_base[r-l]) % self.mod
        return hash
            
    def is_palindrome(self, l, r):
        """S[l:r]が回文かどうかを判定する
        前からのハッシュ値と後ろからのハッシュ値が等しいかどうかで判定"""
        return self.get_hash_forward(l,r) == self.get_hash_backward(l,r)
    
# Input
N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

# ハッシュ計算のパラメータ
base = 10 ** 4 + 7 # 10007 は素数
mod = 10**9 + 7 # 大きな素数

# RollingHashPalindromeクラスの初期化
rh_palindrome = RollingHashPalindrome(S, base, mod)

# クエリ処理
for a,b,c,d in queries:
    # a,b,c,dは1-indexedなので、0-indexedに変換
    hash1 = rh_palindrome.get_hash_forward(a-1, b)
    hash2 = rh_palindrome.get_hash_forward(c-1, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
