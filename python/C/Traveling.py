N = int(input())
count = 0
pt, px, py = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(px-x) + abs(py-y) <= t-pt and t%2 == (x+y)%2:
        count += 1
    pt, px, py = t, x, y
print("Yes" if count == N else "No")
