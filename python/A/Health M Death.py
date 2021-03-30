M,H = map(int, input().split())
if H%M == 0 and H >= M:
    print("Yes")
else:
    print("No")