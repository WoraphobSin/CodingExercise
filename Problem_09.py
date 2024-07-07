a = int(input())
for x in range(0,a):
    for y in range(0,a-x-1):
        print(" ",end="")
    for z in range(0,x*2+1):
        print("*",end="")
    print("")