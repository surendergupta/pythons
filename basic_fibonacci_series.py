num = int(input("Enter the number to find fibonacci Series : "))

n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(0, num, 1):
    temp = n1 + n2
    print(temp)
    n1 = n2
    n2 = temp