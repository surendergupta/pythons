num = int(input("Enter the any number to find it's prime or not : "))

isPrime = True
for i in range(2, num, 1):
    if (num % i == 0) :
        isPrime = False

if isPrime == True :  
    print("Number is prime : ", num)
else : 
    print("Number is not prime : ", num)
    
