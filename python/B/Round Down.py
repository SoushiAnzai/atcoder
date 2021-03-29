X = input()
if X.find(".") != -1:
    print(int(X[:X.find(".")]))
else:
    print(int(X))
# 文字列.find("文字列") "文字列"の位置を取得 ない場合は-1
# 第２引数と第３引数にstart,endを入れられる
# 文字列 in "文字列" "文字列"検索
# 含むtrue 含まないfalse and,orも使用可