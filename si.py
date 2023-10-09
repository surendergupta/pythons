p = int(input("Enter the principal amount: "))
r = float(input("Enter the principal rate: "))
t = int(input("Enter the principal time in years: "))
si = ((p * r * t) / 100)
total = p + si
print(total)
