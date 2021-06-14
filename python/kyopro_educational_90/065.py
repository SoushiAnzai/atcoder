# 赤色のボールが R 個、緑色のボールが G 個、青色のボールが B 個あります。それぞれのボールは、たとえ色が同じであっても互いに区別できます。
# これらの R+G+B 個のボールから、以下の条件を全て満たしながら K 個のボールを選ぶことを考えます。

# - 赤色・緑色のボールを合計 X 個以下選んでいる
# - 緑色・青色のボールを合計 Y 個以下選んでいる
# - 青色・赤色のボールを合計 Z 個以下選んでいる

# このような K 個のボールの選び方は何通りあるでしょうか？
# 答えは非常に大きくなる可能性があるため、答えを 998244353 で割った余りを求めてください。

# 【制約】
# - 1 ≦ R, G, B ≦ 200000
# - 1 ≦ K ≦ min(200000, R+G+B)
# - 0 ≦ X ≦ min(K, R+G)
# - 0 ≦ Y ≦ min(K, G+B)
# - 0 ≦ Z ≦ min(K, B+R)
# - 入力は全て整数

# 【小課題】
# - 小課題 1 (3 点)
#     - 1 ≦ R, G, B ≦ 5
#     - 1 ≦ K ≦ min(5, R+G+B)
# - 小課題 2 (2 点)
#     - 1 ≦ R, G, B ≦ 3000
#     - 1 ≦ K ≦ min(3000, R+G+B)
# - 小課題 3 (2 点)
#     - 追加の制約はない