#  個のブロックが横一列に並んでいます。このブロックの列に色を塗ります。以下では左から i 番目のブロックのことをブロック i と呼ぶことにします。

# 2 つのブロックの列の塗り方が異なるとは、ある 1 以上 N 以下の整数 i が存在して、ブロック i について異なる色で塗られていることと定義します。

# 次の条件を満たすブロック列の塗り方が何通りあるか求めてください。
# ・各ブロックを色 1 からブロック K までのいずれか一色で塗る。使わない色があってもよい。
# ・ブロック i とブロック j について, |i-j|≦2 ならば、ブロック i とブロック j で塗られている色は異なる。
# ただし、答えは非常に大きくなる可能性があるので、 10^9+7 で割った余りを出力してください。

# 【制約】
# ・1 ≦ N ≦ 10^{18}
# ・1 ≦ K ≦ 10^9
# ・入力は全て整数である。