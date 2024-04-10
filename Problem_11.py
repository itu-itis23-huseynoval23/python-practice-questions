# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)

num = int(input("Enter is your number: "))
is_prime = True
 
for i in range (2, int(num * 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print(num, " is prime number")
else:
    print(num, " is not prime number")
        