# names = ["surender", "abhishek", "pankaj", "rohit"]
# feedfacks = [3, 4, 4, 5]

# for i in range(len(names)):
#     if (feedfacks[i] < 4):
#         print(names[i])
#         print(feedfacks[i])

names = []
feedfacks = []

sum = 0
for i in range(0, 5, 1):
    name = input("Please enter a name: ")
    feedfack = input("Please enter a feedback: ")
    names.append(name)
    feedfacks.append(feedfack)
    sum += int(feedfack)

print(f"Average of feedfacks : ", (sum / 5))
