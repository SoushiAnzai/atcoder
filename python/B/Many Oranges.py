import math

A,B,W = map(int, input().split())
W = W*1000
# upper=int(math.floor(W/A))
# lower=int(math.ceil(W/B))
# if lower>upper:
#     print("UNSATISFIABLE")
# else:
#     print(lower,upper)
for i in range(1,1000000):
    if (W-i*A)%B == 0 

