s = input("Enter your number: ")
a = int(s)
while a < 0:
    print("Please input positive number")
    s = input("Enter your number: ")
    a = int(s)
b = int(s + s)
c = int(s + s + s)
d = a + b + c
print(d)
