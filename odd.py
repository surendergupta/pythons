num = int(input("Please enter a limit of odd numbers: "))
sumOfOddNumbers = 0
for i in range(0, num, 1):
    if i % 2 != 0:
        sumOfOddNumbers += i
        print("Odd number: ", i)
print("Odd numbers: ", sumOfOddNumbers)
