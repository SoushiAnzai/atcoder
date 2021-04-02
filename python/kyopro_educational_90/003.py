# N 個の都市があり、それぞれ 1, 2, 3, ..., N と番号付けられています。
# また、N-1 本の道路があり、i 本目の道路は都市 A[i] と都市 B[i] を双方向に結んでいます。
# どの都市の間も、いくつかの道路を通って移動可能なものとなっています。

# さて、あなたは整数 u, v (1 ≦ u < v ≦ N) を自由に選び、都市 u と v を双方向に結ぶ道路を 1 本だけ新設することができます。
# そこで、以下で定められる値をスコアとします。
# ・同じ道を 2 度通らずにある都市から同じ都市まで戻ってくる経路における、通った道の本数
# スコアとして考えられる最大の値を出力してください。

# 【制約】
# ・1 ≦ N ≦ 100000
# ・1 ≦ A[i] < B[i] ≦ N
# ・入力はすべて整数

from collections import deque

# 頂点Uから最も遠い点とその距離を表す関数
def bfs(u):
    dist = [-1]*n
    dist[u] = 0
    q = deque()
    q.append(u)

    while q:
        u = q.popleft()
        for v in to[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                q.append(v)
    mx = max(dist)

    return dist.index(mx), mx

n = int(input())
to = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    to[u].append(v)
    to[v].append(u)

# １度目は任意の頂点から最遠点を求める
u, _ = bfs(0)
# 2度目は１度目で求めた頂点からの最遠点を求める
_, ans = bfs(u)
print(ans+1)