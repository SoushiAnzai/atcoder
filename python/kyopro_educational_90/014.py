# AGC 街道には N 人の小学生が住んでおり、小学生 i の家は位置 A[i] にあります。
# また、小学校は N 校建てられており、小学校 j は位置 B[j] にあります。

# AGC 街道に住む小学生は性格が悪く、どの人同士も険悪な関係になっているため、全員が別の学校に通うようにしたいです。
# また、不便さは次のように定義されます。
# ・小学生 i にとっての家から学校までの距離を E[i] とするとき、不便さは距離の総和、すなわち E[1] + E[2] + ... + E[N] である。
# ・ただし、位置 u から位置 v までの距離は |u-v|

# そこで、どの生徒も別の学校に通うという条件下における、不便さとして考えられる最小値を求めてください。


# 【制約】
# ・1 ≦ N ≦ 100000
# ・0 ≦ A[i] ≦ 10^9
# ・0 ≦ B[i] ≦ 10^9
# ・A[1], A[2], ..., A[N] は相異なる
# ・B[1], B[2], ..., B[N] は相異なる
# ・入力はすべて整数