z = []
sum = 0
for x in range(0,5):
    y = float(input())
    z.append(y)
for i in range(0,5):
    sum = sum + z[i]
average = sum/5
print(f"THAI = {z[0]} \nMATH = {z[1]} \nENGLISH = {z[2]} \nSCIENCE = {z[3]} \nSPORT = {z[4]}")
print("---")
print(f"GPA = {average}")