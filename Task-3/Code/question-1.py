a = int(input("First Number: "))
b = int(input("Last Number: "))

v = []
for i in range(a, b + 1):
    v.append(i)
    for j in range(0, 5):
        v.append(0)
print(v)
