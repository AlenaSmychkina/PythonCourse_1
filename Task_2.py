
a = int(input("Enter time in seconds: "))
while a < 0:
    print ("Please check the right time format")
    a = int(input("Enter time in seconds: "))
h = a//3600
m = (a//60) % 60
s = a % 60
if m < 10:
    m = f"0{m}"
if s < 10:
    s = f"0{s}"
print("{}:{}:{}".format(h, m, s))




