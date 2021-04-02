N = int(input())
# 先に配列を作成する
A = [0 for i in range(N)]
B = [0 for i in range(N)]
for i in range(N):
    A[i],B[i] = map(int,input().split())
if len(A) == 1:
    print(max(A)+max(B))
elif min(A) >= min(B):
    print(min(A))
else:
    print(min(B))