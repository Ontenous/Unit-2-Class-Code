"""
Name: William Nathan
Date: 9/24/24
Description: More on f-strings, input, and numbers/ops
"""

my_int = 5
my_float = 6.38
print(f"{my_int} {my_float}")

another_float = 8.0 #make this a float by adding .0
float_two = float(8) # make a float by casting
print(f"{another_float} {float_two}")

# get decimal from a user
#radius = float(input("Enter a radius: "))
#print(f"You entered a radius of {radius}")

# operations on numbers
# P E MModD AS
# modulus operator or remainder operator
print(15 % 7) # prints the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, times 4

# exponent is not ^, it is **
print(5**4) # this is 5 to the 4
print(5^4) # this is not

# weird math stuff
print(0.3-0.2) # roundoff error - watch out for it

# rounding
# method 1, use round()
num = 3.1415
print(round(num,2))
# method 2, use f string
print(f"{num:.2f}")

#your turn to code
# Ask a user for some amount of US dollars
# Store this in a variable
# Convert that money to some currency of your choice
# Store this conversion factor in a variable
# store the final amount in a variable
# Print it like "___ USD is the same as ___ CAD".
# Round to 2 decimal places

usd = float(input("Please type some amount of US dollars: "))
sol_converter = (3.7515920)
sol_total = float(usd*sol_converter)
print(f"{usd:.2f} USD is the same as {sol_total:.2f} sol")

# string methods
name = "lee cat"
name2 = "BOB BUILDER"
print(name.upper())
print(name.title())
print(name2.lower())