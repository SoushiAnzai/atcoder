# 白石と青石からなる山が N 個あり、左から右に並んでいます。
# 左から i 番目の山には最初、白石が W[i] 個、青石が B[i] 個あります。

# あなたと E869120 が、この石の山を用いて以下のゲームを行います。

# > 各ターンには、山をひとつ選び、選んだ山に対して [A], [B] いずれかの操作を 1 回行う。
# > 
# >     [A] 選んだ山に青石を w 個加え、白石を 1 個取り除く。
# >     [B] 1 以上 floor(b/2) 以下の整数 k を選び、選んだ山から青石を k 個取り除く。
# > 
# > ただし、[A] は w ≧ 1 の場合、[B] は b ≧ 2 の場合にしか操作を行うことができない。
# > なお、w は選んだ山にあるその時点での白石の個数、b は選んだ山にあるその時点での青石の個数とする。

# 自分のターンが回ってきたときに、操作を行えなくなった方が負けです。
# あなたが勝つためには、先攻・後攻どちらを選べばよいですか？


# 【制約】
# ・1 ≦ N ≦ 10^5
# ・0 ≦ W[i] ≦ 50
# ・0 ≦ B[i] ≦ 50
# ・(W[i], B[i]) ≠ (0, 0)
# ・入力はすべて整数