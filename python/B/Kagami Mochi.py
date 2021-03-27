N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))
# set() 重複削除
# len() 要素数,文字列の場合は文字数