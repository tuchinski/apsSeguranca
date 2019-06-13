import crypt
import string
from random import choice

def createPassword():
    userPassword = input("Digite a nova senha:")
    arq = open('/etc/shadow')

    # Starting salt creation
    salt = '$6$'

    # All alphanumeric ascii
    possibleSalt = string.ascii_letters + string.digits

    # Creating salt password
    for a in range(8):
        salt = salt + choice(possibleSalt)
    salt = salt + '$'


    encriptedPassword = crypt.crypt(userPassword,salt)

    print(encriptedPassword)

if __name__ == "__main__":
    createPassword()