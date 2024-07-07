a = int(input())

if (a%4) == 0:
    if (a%100) != 0 or (a%400) == 0:
        if(a%400) == 0 or (a%4) == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a Leap Year")