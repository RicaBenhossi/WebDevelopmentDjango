import hashlib
import cryptography


# passwdhash = hashlib.sha1(input('senha:\n').encode("utf-8"))
senha = str(input('senha:\n')) 
passwdhash = hashlib.md5(senha.encode("utf-8"))

#passwdhash.digest()
print(passwdhash)
print(passwdhash.hexdigest())