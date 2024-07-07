x = []
j = int(input())
for y in range(0,j):
    z = int(input())
    x.append(z)
x.sort()
for i in range(0,j):
    print(x[j-1-i])