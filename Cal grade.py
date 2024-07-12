a = int(input())
if a>=0 and a<=100:
    if a>=90:
        print("A")
    elif a>=85:
        print("B+")
    elif a>=80:
        print("B")
    elif a>=75:
        print("C+")
    elif a>=70:
        print("C")
    elif a>=65:
        print("D+")
    elif a>=60:
        print("D")
    else:
        print("F")
elif a<0:
    print("Error : Value must be greater than or equal to 0.")
else:
    print("Error : Value must be less than or equal to 100.")