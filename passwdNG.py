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

    user_change = "false"
    # print(encriptedPassword)
    fileShadow = open('/etc/shadow')
    conteudo = fileShadow.readlines()
    fileShadowRead = fileShadow.read().split()
    for line in fileShadowRead:
        lineBreak = line.split(':')
        if(lineBreak[0] == userName):
            print(encriptedPassword)
            lineBreak[1] = encriptedPassword
            print(lineBreak)
            user_change = "true"
            #fileShadow.write(makeLineShadow(lineBreak))
            break
 
    if user_change == "false":
        print ("Este usuario não esta presente sistema")       
            


def makeLineShadow(lineBreak):
    new_line = ""
    for i in lineBreak:
        new_line = new_line + i +":"
    return new_line[:-1]

    # print(len(fileShadowRead))
    



if __name__ == "__main__":
    createPassword()