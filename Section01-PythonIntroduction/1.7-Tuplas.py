"""
TUPLE

Tuple look alike list bt they are not changeble. They ar simbolized by ()
Can contain a lot of variables into it.
"""

# The tuple TUP cointains in order:
# string data, integer, double, a list and another tupla.
tup = ("Python", "Java", 1, 9.8, [7, 14, 21], ("Elixir", "Android", 3, 5.1, [3, 6, 9]))
type(tup)
print(tup)
print(tup[0])
print(tup[4])
print(tup[5])

# Although a tuple can not be changed, if we have a list inside it, this list can be changed.
tup[4].append("New Data")
print(tup[4])
