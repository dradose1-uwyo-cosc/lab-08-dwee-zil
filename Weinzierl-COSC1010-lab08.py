# Mak Weinzierl
# UWYO COSC 1010
# November 7, 2024
# Lab 08
# Lab Section: 12
# Sources: Textbook

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_string(string):
    """Check if a string is an integer or float and convert it if so"""
    if type(string) != str:
        return string
    elif string.isdigit():
        string = int(string)
        return string
    elif string[0] == "-":
        if string.replace("-","",1).isdigit():
            string = int(string)
            return string
        elif "." in string:
            if string.replace("-","",1).replace(".","",1).isdigit():
                string = float(string)
                return string
            else:
                return False
        else:
            return False
    elif "." in string:
        if string.replace(".","",1).isdigit():
            string = float(string)
            return string
        else:
            return False
    else:
        return False

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,lower_x,upper_x):
    """Output the y-values of a y = mx + b equation given x bounds"""
    if type(m) == str:
        m = convert_string(m)
    if not convert_string(m):
        return False
    if type(b) == str:
        b = convert_string(b)
    if not convert_string(b):
        return False
    if type(lower_x) == str:
        lower_x = convert_string(lower_x)
    if not convert_string(lower_x):
        return False
    if type(upper_x) == str:
        upper_x = convert_string(upper_x)
    if not convert_string(upper_x):
        return False
    
    if type(lower_x) == float:
        return False
    if type(upper_x) == float:
        return False
    if lower_x > upper_x:
        return False
    
    y_values = []
    for value in range(lower_x,upper_x + 1):
        y_values.append(m*value + b)
    return y_values

while True:
    print("Hello! Please enter a slope, y-intercept, lower x bound, and upper x bound for a y = mx + b equation to determine its y-values.")
    print("Enter 'exit' to exit.")
    
    m = input("Enter the slope here: ")
    if m.lower() == "exit":
        break
    b = input("Enter the y-intercept here: ")
    if b.lower() == "exit":
        break
    lower_x = input("Enter the lower x bound here: ")
    if lower_x.lower() == "exit":
        break
    upper_x = input("Enter the upper x bound here: ")
    if upper_x.lower() == "exit":
        break
    
    if not slope_intercept(m,b,lower_x,upper_x):
        print(f"\nMake sure the m and b are integers or floats, the x bounds are integers, and the lower bound is less than the upper bound.\n")
    else:
        print(f"\n{slope_intercept(m,b,lower_x,upper_x)}\n")
            
print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quad_formula_sqrt(a,b,c):
    """Output the value of the square root operation of the quadratic formula"""
    if type(a) == str:
        a = convert_string(a)
    if type(b) == str:
        b = convert_string(b)
    if type(c) == str:
        c = convert_string(c)
    
    sqrt_entry = (b**2 - (4*a*c))
    if sqrt_entry >= 0:
        sqrt = sqrt_entry**0.5
        return sqrt
    else:
        return None
    
def quad_formula(a,b,c):
    """Output the values of the quadratic formula"""
    if type(a) == str:
        a = convert_string(a)
    if type(b) == str:
        b = convert_string(b)
    if type(c) == str:
        c = convert_string(c)
    if not quad_formula_sqrt(a,b,c):
        return None
    else:
        outputs = []
        x_1 = (-b + quad_formula_sqrt(a,b,c))/(2*a)
        x_2 = (-b - quad_formula_sqrt(a,b,c))/(2*a)
        outputs.append(x_1)
        outputs.append(x_2)
        return outputs
    
while True:
    print("Hello! Please enter an a, b, and c for a y = ax^2 + bx + c equation to determine its x-intercepts.")
    print("Enter 'exit' to exit.")

    a = input("Enter your a here: ")
    if a.lower() == "exit":
        break
    b = input("Enter your b here: ")
    if b.lower() == "exit":
        break
    c = input("Enter your c here: ")
    if c.lower() == "exit":
        break
    
    if not quad_formula(a,b,c):
        print(f"\nThere are no x-intercepts for that equation.\n")
    else:
        print(f"\n{quad_formula(a,b,c)}\n")