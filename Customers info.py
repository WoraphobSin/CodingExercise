x = int(input())
i = [] # Name
j = [] # Year of birth
k = [] # Gender
year = 2017
for y in range(0,x):
    a = input()
    b = int(input())
    c = input()
    i.append(a)
    j.append(2017-b)
    k.append(c)
print("--Customers Information--")
for m in range(0,x):
    print(f"{i[m]} (age : {j[m]})")