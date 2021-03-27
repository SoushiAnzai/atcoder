N,A,B = map(int, input().split())
print(sum(i for i in range(1,N+1) if A <= sum(map(int, str(i))) <= B))
# sum(i for i in <反復可能オブジェクト>) 反復したすべてのiを合計する