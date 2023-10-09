learners = []
sum = 0
for i in range(0, 5, 1):
    learner = {}
    name = input("Please enter a name: ")
    feedfack = input("Please enter a feedback: ")
    learner["name"] = name
    learner["feedback"] = feedfack
    learners.append(learner)
    sum += int(feedfack)
print(learners)
print(f"Average of feedfacks : ", (sum / 5))
