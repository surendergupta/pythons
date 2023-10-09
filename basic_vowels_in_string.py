vowelString = input("Enter string to count number of vowel in string : ")
con = 0
for i in range(len(vowelString)):
    if vowelString[i] == 'a' or vowelString[i] == 'e' or vowelString[i] == 'i' or vowelString[i] == 'o' or vowelString[i] == 'u' : 
        con = con + 1
print("number of vowel in string : ", con)