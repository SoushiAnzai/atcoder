# Aが無乳、Bが乳脂肪、Cが乳固形
A,B = map(int, input().split())
C = A+B
if C >= 15 and B >= 8:
    print(1)
elif C >= 10 and B >= 3:
    print(2)
elif C >= 3:
    print(3)
else:
    print(4)