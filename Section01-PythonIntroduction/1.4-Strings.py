"""
    Strings are texts and must come between quotation marks
"""

x = "Python"
y = "Class"
# The command "type returns the type of a variable. In this case a String or str
print("Printing Strings variables")
print("Variable x has the value: " + x + " and the type: " + str(type(x)))
print(y + str(type(y)))

# We can concatenate or plus the variables

# Command \n breakes line
print("\nPrinting a concatenated strings")
print(x + " " + y)
z = y + x 
print(z)

# String are lists of characters, so they accept indexes started in 0
print("\nPrinting index strings")
print(x[3])
print(y[2] + x[2])

# We can also slice it use a range in the indexes
print("\nPrinting slices of a string")
# in this case we print from index 2 to 5
print(y[2:5])
# in this case we print from index 0 to 2
print(x[:2])
# in this case we print from index  to the last one
print(y[3:])
# we can also use a negative index
print(x[-2])
print(x[:-2])
print(x[-2:])