carPerHour = 20
bikePerHour = 10
parkingPerDay = 6

noOfCars = int(input("Please enter number of car: "))
noOfBikes = int(input("Please enter number of bike: "))

totalPaymentCollection = 0
if noOfCars > 0:
    totalPaymentCollection += noOfCars * carPerHour * parkingPerDay
elif noOfBikes > 0:
    totalPaymentCollection += noOfBikes * bikePerHour * parkingPerDay

if totalPaymentCollection > 10000:
    print("It is good day have some profits")
else:
    print("It is bad day not have enough")
