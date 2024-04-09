# Create a program that asks the user for a number and 
# then prints out a list of all the divisors of that number.
num = int(input("What is your number: "))
a = []
for i in range(1,num+1):
    if num % i == 0:
        a.append(i)

print(a)