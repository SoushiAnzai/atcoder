S = input()
print(S[1:len(S)] + S[0:1])


H,W,X,Y = map(int, input().split())
s = [input() for i in range(H)]
up = s[X-2][Y-1]
dp = s[X][Y-1]
lp = s[X-1][Y-2]
rp = s[X-1][Y]
count = 1
for i in range(X-1):
    if s[X-2-i][Y-1] == "." and X-2-i >= 0 and Y-1 >= 0:
        count += 1
    else:
        break
for i in range(H-X):
    if s[X+i][Y-1] == "." and X+i >= 0 and Y-1 >= 0:
        count += 1
    else:
        break
for i in range(Y-1):
    if s[X-1][Y-2-i] == "." and X-1 >= 0 and Y-2-i >= 0:
        count += 1
    else:
        break
for i in range(W-Y):
    if s[X-1][Y+i] == "." and X-1 >= 0 and Y+i >= 0:
        count += 1
    else:
        break
print(count)



N = int(input())
