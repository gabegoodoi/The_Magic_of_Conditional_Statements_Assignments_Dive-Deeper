# Task 1: Identify the Greatest:
# Write a Python program that asks the user to enter three numbers. Your code 
# should then identify and print out the largest number among the three.

number_a = int(input("enter a number: "))
number_b = int(input("enter a number: "))
number_c = int(input("enter a number: "))

#Commented out for alt version, first I wrote this, but I felt like it could read simpler, so I revised to below. Not sure which is better.
# if number_a > number_b and number_a > number_c:
#     print(number_a)
# elif number_b > number_a and number_b > number_c:
#     print(number_b)
# elif number_c > number_b and number_c > number_a:
#     print(number_c)

# commented out for task 2
# if number_a <= number_b:
#     high_number = number_b
#     if high_number <= number_c:
#         print(f"{number_c} is the largest number")
#     else:
#         print(f"{high_number} is the largest number")
# else:
#     print(f"{number_a} is the largest number")

# Task 2: Identify the Smallest:
# Improve upon your code from Task 1 to also the smallest number among the 
# three and print it out.

if number_a >= number_b:
    low_number = number_b
    high_number = number_a
else:
    low_number = number_a
    high_number = number_b
if low_number >= number_c:
        low_number = number_c
elif number_c >= high_number:
    high_number = number_c
print(f"The smallest number is {low_number}. The largest number is {high_number}.") 

# Expected Outcome: 
# If we provide the numbers 3, 3, and 4, it should print out that "The smallest 
# number is 3. The largest number is 4. "

