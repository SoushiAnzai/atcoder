# 縦 H マス、横 W マスからなるグリッドがあり、上から i 番目・左から j 番目のマスを (i, j) で表します。
# 各マスには色が塗られており、マス (i, j) の色は C[i][j] = '#' のとき黒、C[i][j] = '.' のとき白です。

# あなたはいくつかの白マスを選び（1 つも選ばなくても良い）、キングの駒を置きます。
# キング同士が互いに攻撃し合わないような置き方の数を 10^9+7 で割った余りを求めてください。
# ただし、ある 2 つの置き方が異なるとは、「ある白マスが存在して、片方ではキングが置かれており、もう片方では置かれていない」ことを言います。

# ＜キング同士が互いに攻撃し合わない、とは＞
# ・キングが置かれている任意の異なる 2 マス (i, j) および (k, l) において、|i-k|>1 または |j-l|>1 が成り立つことを言います。

# 【制約】
# ・1 ≦ H, W ≦ 24
# ・H, W は整数
# ・C[i][j] は '#' または '.'
# ・少なくとも 1 つの白マスが存在する

# 【小課題】
# 1. (1 点) 1 ≦ H, W ≦ 4
# 2. (1 点) 1 ≦ H, W ≦ 9
# 3. (2 点) 1 ≦ H, W ≦ 17
# 4. (3 点) 追加の制約はない