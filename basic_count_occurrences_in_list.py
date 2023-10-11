from collections import Counter
useList = [55,89,52,36,15,2,84, 835, 36, 89, 55, 1, 35]
print("Please select any one number in List : ", useList)
num = int(input("Enter the number to find count number in list : "))
print("Count Number : ", useList.count(num))


print("All Count Number : ", Counter(useList))
