"""
LOOP STRUCTURES

Python has only 2 types of loop: FOR and WHILE.
"""

def teste()

# FOR structure: run an instruction for X times.
lang = "Python"
for x in lang:
    print(x)
print()
for y in range(10):
    print(y)

# WHILE executes unless 1 time and there is no explicit stop point
controler = 10
while controler >= 0:
    print("Countdown: ", controler)
    controler -= 1
    if (controler < 0):
        print("DONE!")

list_a = [3, 9, 17, 15, 19]
list_b = {'a': 2, 'b': 4, 'c': 8, 'd': 10, 'e': 30}
