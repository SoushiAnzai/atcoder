N = int(input())
A = list(map(int, input().split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)
# イテラブルオブジェクト⇢反復可能なオブジェクト
# 　　　　　　　　　　　　シーケンス型(リスト、タプル、range)
# 　　　　　　　　　　　　マッピング型(辞書)
# 　　　　　　　　　　　　テキストシーケンス型(文字列)
# 　　　　　　　　　　　　バイナリシーケンス型(bytes、bytearray、memoryview)
# all() イテラブルオブジェクトがすべてtrueかを判定
# any() イテラブルオブジェクトのいずれかがtrueを判定
# not any() イテラブルオブジェクトがすべてfalseかを判定