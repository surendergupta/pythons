numList = [55,89,52,36,15,2,84]
strList = ["Surender", "Pankaj", "Komal", "Ravinder", "Jadeja", "Tailor", "Bhubneshwar"]

# sort ASC
numList.sort(reverse=False)
strList.sort(reverse=False)

print("Ascending Order List : ", numList)
print("Ascending Order List : ", strList)

# sort DESC
numList.sort(reverse=True)
strList.sort(reverse=True)

print("Descending Order List : ", numList)
print("Descending Order List : ", strList)