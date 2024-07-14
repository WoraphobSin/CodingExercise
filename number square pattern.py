# ข้อ 7
z = int(input())

for a in range(1,z+1):
    for b in range(1,a+1):
        print(b,end="")
    for c in range(1,2*(z-a)+1):
        print(a,end="") 
    for e in range(1,a):
        print(a-e,end="") 
    print()


for x in range(1,z):
    for y in range(1,z-x+1):
        print(y,end="")
    for i in range(1,2*x):
        print(z-x,end="")
    for j in range(1,z-x+1):
        print(z-x-j+1,end="")
    print("")
