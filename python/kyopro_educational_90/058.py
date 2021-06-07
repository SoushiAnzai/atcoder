# あなたは奇妙な電卓を持っています。この電卓は 0 以上 99999 ( = 10^5-1) 以下の整数を 1 つ表示できます。電卓には ボタンA があり、これを 1 回押すと、次の処理が順番に行われます。

# > 現在電卓に表示されている整数を x とする。
# > 1. x を十進法で表したときの各桁の和を計算し、これを y とする。
# > 2. 電卓に表示される整数を「x+y を 10^5 で割ったあまり」に変更する。

# いま、この電卓に N が表示されています。 ボタンA を K 回押した後に表示されている整数を求めて下さい。

# 【制約】
# ・0 ≦ N ≦ 99999 ( = 10^5-1)
# ・1 ≦ K ≦ 10^18
# ・入力はすべて整数