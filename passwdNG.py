import crypt
import string
from random import choice

def createPassword():
    userName = input('Digite o nome do usuário:')
    userPassword = input("Digite a nova senha:")

    # Starting salt creation
    salt = '$6$'

    # All alphanumeric ascii
    possibleSalt = string.ascii_letters + string.digits

    # Creating salt password
    for a in range(8):
        salt = salt + choice(possibleSalt)
    salt = salt + '$'
    

    encriptedPassword = crypt.crypt(userPassword,salt)

    # print(encriptedPassword)
    fileShadow = open('/etc/shadow')
    fileShadowRead = fileShadow.read().split()
    for line in fileShadowRead:
        lineBreak = line.split(':')
        if(lineBreak[0] == userName):
            lineBreak[1] = encriptedPassword
            print(lineBreak)
            # print('aqui')
            break


    
    # print(len(fileShadowRead))
    



if __name__ == "__main__":
    createPassword()