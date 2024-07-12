a = int(input())
if a>0 or a<100:
    for x in range(0,a):
        if x == 0 or x == a-1:
            for x in range(0,a):
                print("#",end="")
            print("")
        else:
            print("#",end="")
            for y in range(0,a-2):
                print(" ",end="")
            print("#")
