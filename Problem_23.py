a = int(input())
c = 1
if a>0 and a<100:
    for b in range(0,a):
        c = c*(b+1)
    print(c)
elif a == 0:
    print(c)