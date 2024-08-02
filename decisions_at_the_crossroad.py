# Task 1: Code Correction You are provided with a Python script that 
# uses conditional statements to tell if a number is positive, negative, 
# or zero, but it has some errors. Identify and fix them.

# Buggy Code:
# number = input("Enter a number: ")
# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

# implemented type conversion to integer for input string
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
# changed elif statememnt to change the assignment operator = to comparitive operator ==
elif number == 0:
    print("The number is zero.")
# changed the else statement to remove conditions
else:
    print("The number is negative.")