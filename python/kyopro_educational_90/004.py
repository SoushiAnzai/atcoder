# H 行 W 列のマス目があります。上から i (1 ≦ i ≦ H) 行目、左から j (1 ≦ j ≦ W) 列目にあるマス (i, j) には、整数 A[i][j] が書かれています。

# すべてのマス (i, j) [1 ≦ i ≦ H, 1 ≦ j ≦ W] について、以下の値を求めてください。
# ・マス (i, j) と同じ行または同じ列にあるマス（自分自身を含む）に書かれている整数をすべて合計した値

# 【制約】
# ・1 ≦ H ≦ 2000
# ・1 ≦ W ≦ 2000
# ・1 ≦ A[i][j] ≦ 99
# ・入力はすべて整数

h,w = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(h)]

# 行ごとの和
rs = [sum(row) for row in a]
# 列ごとの和
cs = [sum(col) for col in zip(*a)]
# *List リストの中身だけ一つずつ関数に渡す
ans = [[rs[i]+cs[j]-a[i][j] for j in range(w)] for i in range(h)]

for row in ans: print(*row)