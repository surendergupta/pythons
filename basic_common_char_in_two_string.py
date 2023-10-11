str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")

# using sets and inersection
print(''.join(set(str1).intersection(str2)))

# using loop
uchar = [i for i in set(str1) if i in str2]

print(''.join(uchar))
