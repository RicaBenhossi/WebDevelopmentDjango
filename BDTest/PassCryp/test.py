from simplecrypt import encrypt, decrypt


passwd = str(input('Digite a senha: '))
print(passwd)
passwd_crypt = encrypt('', passwd).decode('utf-8')
print(passwd_crypt)
passwd_decrypt = decrypt('', passwd_crypt).decode('utf-8')