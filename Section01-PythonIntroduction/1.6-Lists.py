"""
Lists are variables with an index, like an array. Use [] to set a list
Use DIR to see all the methods this variable acceppts
"""
vListVar = []
print(type(vListVar))

# APPEND: add a data to your list.
vListVar.append('Python')
print(vListVar)
vListVar.append('Java')
print(vListVar)
vListVar.append('PHP')
vListVar.append('Delphi')

# REVERSE: invert the rder off all components of the list
print(vListVar)
vListVar.reverse()
print(vListVar)
# a new revers, ofcourse returns the list to the original order.
print(vListVar.reverse())

# INSERT: inset a data in an index you want.It takes 2 parameters:
    # the position you want to add the new data (integer started at 0)
    # the data itself
vListVar.insert(2, 'Go')
print(vListVar)

# POP: removes the last element of the list and return it.
vListVar.pop()
print(vListVar)

# COUNT: returns how many times a data shows in the list
print(vListVar.count('Go'))

#REMOVE: removes a data from the list
vListVar.remove('Java')
print(vListVar)

# A list can contain any type of variables, including another list
vListVar.append(3)
vListVar.append(2.8)
print(vListVar)
vList2 = [1, 2, 3]
vListVar.append(vList2)
print(vListVar)