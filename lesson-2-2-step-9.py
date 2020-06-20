import simplecrypt


with open("encrypted (1).bin", "rb") as inp:
    encrypted = inp.read()
    with open("passwords.txt", "r") as password_file:
        for password in password_file:
            try:
                print(simplecrypt.decrypt(password.strip(), encrypted))
            except simplecrypt.DecryptionException:
                pass


# Ответ
# Alice loves Bob
