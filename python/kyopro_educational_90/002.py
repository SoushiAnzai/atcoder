N = int(input())

# 2進法で表したときの１の個数
def popcnt(bit):
    return bin(bit).count("1")
# bin() 引数に指定した整数を2進数表現の文字列に変換

def solve(bit):
    # 0と1の個数が違ったらNG
    if popcnt(bit) != N//2: return
    # 0を"("に1を")"に置き換え
    ans = ""
    for _ in range(N):
        if bit & 1: ans += ")"
        else: ans += "("
        bit >>= 1
        # >> ビット右シフト
        # a>>=b a=a>>bと同じ
    ans = ans[::1]
    # 途中で"("より")"の個数が多くなったらNG
    now = 0
    for c in ans:
        if c == "(": now += 1
        else: now -= 1
        if now < 0:return
    print(ans)

if N & 1: exit()
# AND:論理積(aもbも1のビットが1)

for bit in range(1 << N):
    solve(bit)