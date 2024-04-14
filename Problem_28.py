# Implement a function that takes as input three variables, and returns the largest of the three.

def max_of_three(a,b,c):
     max=0
     if a>b:
         #max=a
         if a>c:
             max=c
         else:
             max=a
     else:
          if b>c:
             max=b
          else:
             max=c
     return max

a,b,c = int(input("Enter the numbers:"))
result = max_of_three(a,b,c)
print(f"The largest number is {result}")
