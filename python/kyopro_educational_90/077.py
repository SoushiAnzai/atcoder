# 2次元座標平面とみなせる大空をN機の飛行機が航行しています。
# i=1,2,...,Nに対し、i番目の飛行機は時刻0において座標 (AX[i],AY[i]) に存在しました。

# 飛行機はいずれも向き1,2,3,4,5,6,7,8のいずれかを向いて航行しています。
# 時刻tにおいて (x,y) に存在する向きdの飛行機は、時刻t+1において
# ・d=1ならば (x+1,y) に
# ・d=2ならば (x+1,y+1) に
# ・d=3ならば (x,y+1) に
# ・d=4ならば (x-1,y+1) に
# ・d=5ならば (x-1,y) に
# ・d=6ならば (x-1,y-1) に
# ・d=7ならば (x,y-1) に
# ・d=8ならば (x+1,y-1) に
# 存在します。
# また、航行の途中で飛行機が向きを変えることはありません。

# あなたは管制官の高橋くんから次のような報告を受けました。

# ・時刻Tにおいて、座標 (BX[1],BY[1]),(BX[2],BY[2]),...,(BX[N],BY[N]) に飛行機が存在した

# 彼の報告に矛盾しないようなN機の飛行機の向きの組み合わせが存在するかを判定し、存在する場合は一つ出力してください。

# 【制約】
# ・1≦N≦20000
# ・1≦T≦10^9
# ・0≦AX[i],AY[i],BX[i],BY[i]≦10^9
# ・i≠jならば(AX[i],AY[i])≠(AX[j],AY[j])
# ・i≠jならば(BX[i],BY[i])≠(BX[j],BY[j])
# ・入力はすべて整数

# 【小課題】
# 1.(1 点) N≦6
# 2.(1 点) AY[i]=0,BY[i]=0
# 3.(2 点) N≦1000
# 4.(3 点) 追加の制約はない