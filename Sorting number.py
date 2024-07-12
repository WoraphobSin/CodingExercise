x = []
j = int(input())
for y in range(0,j):
    z = int(input())
    x.append(z)
x.sort()
print(x)
for i in range(0,j):
    print(x[j-i-1])