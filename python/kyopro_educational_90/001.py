# 長さ L [cm] のようかんがあります。
# N 個の切れ目が付けられており、左から i 番目の切れ目は左から A[i] [cm] の位置にあります。

# あなたは、N 個の切れ目のうち K 個を選び、ようかんを K+1 個のピースに分割したいです。そこで、以下の値をスコアとします。
# ・K+1 個のピースのうち、最も短いものの長さ
# スコアが最大になるように分割する場合に得られるスコアを求めよ。

# 【制約】
# ・1 ≦ K < N ≦ 10^5
# ・0 ≦ A[1] < A[2] < ... < L ≦ 10^9
# ・入力はすべて整数

# 【入力形式】
# N L
# K
# A[1] A[2] A[3] ... A[N]

N,L = map(int, input().split())
K = int(input())
# 切れ目＋左端と右端のList
aa = [0]+list(map(int, input().split()))+[L]
# すべて切ったときの一つずつの長さ
dd = [a1-a0 for a0, a1 in zip(aa, aa[1:])]

# 長さの最小値をmとする
# m以上のかたまりを作っていったときに、k+1個以上できるか？
def ok(m):
    now = 0
    cnt = 0
    for d in dd:
        now += d
        if now >= m:
            cnt += 1
            if cnt == k+1: return True
            now = 0
    return False

# 最小値の最大化=>二分探索
l, r = 0, L
while l+1 < r:
    m = (l+r)//2 # //は割り算切り捨て
    if ok(m): l = m
    else: r = m

print(l)