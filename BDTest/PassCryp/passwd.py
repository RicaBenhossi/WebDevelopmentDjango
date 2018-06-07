import hashlib


passwdhash = hashlib.md5()

passwdhash = hashlib.sha1(input('senha:\n').encode("utf-8"))
#passwdhash.digest()
print(passwdhash)
print(passwdhash.hexdigest())