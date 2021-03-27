a = int(input())
b, c = map(int, input().split())
s = input()
print("{} {}".format(a+b+c, s))

# input() 入力値取得
# int(input()) 入力値（数値）取得
# print() 出力
# {format}.format() formatに整形して出力（{}で引数設定可）