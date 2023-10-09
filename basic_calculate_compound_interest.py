# p stands for principle amount  
# r stands for rate of interest
# t stands for time
# ci = p(1+r/n)nt
p = int(input("Plese enter a principal amoun : "))
r = float(input("Plese enter a rate of interest : "))
t = float(input("Plese enter a time period loan : "))
r =  (r /100)
n = 12
ci = (p * ( 1 + r/n) ** (n * t))

print("Compound interest of your loan: ", ci)
print("Total interest of your loan: ", (ci - p))