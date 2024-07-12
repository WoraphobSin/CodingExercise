
all_weight = []
while True:
    weight = int(input()) 
    if weight == 0:
        x= str(input())
        y = x.lower()
        if y == "max":
            all_weight.sort(reverse=True)
            for z in range(0,len(all_weight)):
                print(all_weight[z],end=" ")
            break
        elif y == "min":
            all_weight.sort()
            for z in range(0,len(all_weight)):
                print(all_weight[z],end=" ")
            break
    else:
        all_weight.append(weight)

