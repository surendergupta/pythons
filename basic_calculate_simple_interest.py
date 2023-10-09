# p stands for principle amount  
# r stands for rate of interest
# t stands for time
# si = p * r * t/12 /100
p = int(input("Plese enter a principal amoun : "))
r = float(input("Plese enter a rate of interest : "))
t = float(input("Plese enter a time period loan : "))

si = ((p * r * t)/100)

print("Simple interest of your loan: ", si)
print("Total payment with interest of your loan: ", p + si)