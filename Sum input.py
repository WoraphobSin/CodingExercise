x = int(input())
y = []
sum = 0
for z in range(0,x):
    i = int(input())
    y.append(i)
for j in range(0,x):
    sum = sum + y[j]
print(f"{sum} THB")