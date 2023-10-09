num = int(input("Please enter number to find factorial: "))
fact = 1
for i in range(num+1):
    if i == 0 : 
        continue
    else:
        fact = fact * i
print(f"Factorial of ",num, " is :",fact)