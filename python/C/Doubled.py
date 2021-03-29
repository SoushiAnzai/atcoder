N = int(input())
count = 0
for inti in range(N):
    i = str(inti)
    if len(i)%2 == 0:
        if len(i) == 0:
            length = 0
        else:
            length = int(len(i)/2)
        if i[:length-1:] == i[length::]:
            count += 1
print(count)

N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()