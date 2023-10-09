number = [33, 74, 94, 45, 25, 15, 39, 85]
sum = 0
for i in range(len(number)):
    if number[i] % 2 == 0:
        sum = sum + number[i]    

print("Sum of given list of numbers : ", sum )