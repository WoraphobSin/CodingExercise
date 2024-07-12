
num = []
sum = 0
i = 0
def sep(text):
    for x in range(0,len(text)):
        count = text[x:x+1]
        num.append(count)
    return num

def summation(num): 
    global sum
    sum = 0   
    for y in range(0,len(num)):
        sum = sum + int(num[y])
    return sum

text = input()
while len(text) > 1:
    sep(text)
    summation(num)
    num.clear()
    text = str(sum)
    i = i+1
print(text)
print(i)