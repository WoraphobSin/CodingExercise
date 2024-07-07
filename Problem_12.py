message = input()
txt = message.split()
for x in range(0,len(txt)):
    print(f"{txt[len(txt)-x-1]}",end=" ")
