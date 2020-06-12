maxvalue = 0
s = int(input("Enter your number: "))
while s != 0:
    a = s % 10
    if a > maxvalue:
        maxvalue = a
    s = s // 10
print(maxvalue)

