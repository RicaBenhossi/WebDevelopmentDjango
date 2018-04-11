"""
DICTIONARY

This type of data has not an integer index, you can define the keys of indexation
It uses {} to identify this typos of data.
"""

# You can have all kind of data as an index key, but not Lists because they are changeble.
dic = {"key": 1, 5: 10, 2.5: "AUR", "A List": [1, 3, 5, 7], "Item1": 22}
type(dic)
print(dic)
print(dic[2.5])
print(dic["A List"])

# If you have a list in a position, you can edit it
dic["A List"].append("A new value")
print(dic["A List"])

# To remove a key, you can use POP
print(dic)
dic.pop(5)
print(dic)

# POPIEM removes the last key in the dictionary
dic.popitem()
print(dic)
